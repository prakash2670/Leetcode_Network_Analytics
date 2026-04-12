from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
import time

options = Options()
# options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

all_problems = []
# --Step1--
driver.get("https://leetcode.com/problemset/")
time.sleep(3)  # wait for page to load

driver.execute_script("""
    window._interceptedData = [];
    const origFetch = window.fetch;
    window.fetch = function(...args) {
        return origFetch.apply(this, args).then(async res => {
            const clone = res.clone();
            try {
                const body = await clone.json();
                if (body?.data?.problemsetQuestionList) {
                    window._interceptedData.push(body);
                }
            } catch(e) {}
            return res;
        });
    };
""")

print("Waiting for LeetCode to load problems...")
time.sleep(5)

# ── Step 2 ──
page = 1
while True:
    print(f"Loading page {page}...")

    try:
        next_btn = driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="next"]'
        )
        if not next_btn.is_enabled():
            print("Last page reached.")
            break
        next_btn.click()
        time.sleep(2)
        page += 1
    except Exception:
        print("No next button found, stopping.")
        break

# ── Step 3 ──
intercepted = driver.execute_script("return window._interceptedData;")
print(f"\nIntercepted {len(intercepted)} GraphQL responses")

for batch in intercepted:
    questions = batch["data"]["problemsetQuestionList"]["questions"]
    for q in questions:
        try:
            stats = json.loads(q.get("stats", "{}"))
            total_submissions = stats.get("totalSubmissionRaw", "N/A")
            total_accepted    = stats.get("totalAcceptedRaw", "N/A")
        except Exception:
            total_submissions = "N/A"
            total_accepted    = "N/A"

        try:
            similar = json.loads(q.get("similarQuestions", "[]"))
            similar_problems = ", ".join(
                str(p.get("frontendQuestionId", "")) for p in similar
            )
        except Exception:
            similar_problems = ""

        all_problems.append({
            "number":            q.get("questionFrontendId"),
            "title":             q.get("title"),
            "difficulty":        q.get("difficulty"),
            "tags":              ", ".join(t["name"] for t in q.get("topicTags", [])),
            "total_submissions": total_submissions,
            "total_accepted":    total_accepted,
            "accepted_rate":     round(q["acRate"], 2) if q.get("acRate") else "N/A",
            "similar_problems":  similar_problems,
        })

driver.quit()

print(f"\nTotal problems scraped: {len(all_problems)}")

csv_fields = [
    "number", "title", "difficulty", "tags",
    "total_submissions", "total_accepted",
    "accepted_rate", "similar_problems"
]

with open("leetcode_selenium.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_fields)
    writer.writeheader()
    writer.writerows(all_problems)

print("Saved to leetcode_selenium.csv")

with open("leetcode_selenium.json", "w") as f:
    json.dump(all_problems, f, indent=2)

print("Saved to leetcode_selenium.json")
