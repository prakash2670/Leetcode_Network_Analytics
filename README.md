# 📊Leetcode_Network_Analytics

## 🚀 Overview
This project applies **network science techniques** to analyze the structure of the LeetCode problem set. Instead of approaching problems sequentially or randomly, the dataset is modeled as a graph to uncover **patterns, relationships, and efficient learning strategies**.

Problems and their associated topic tags are represented as networks, enabling a structured and data-driven understanding of the problem space.

---

## 🎯 Objectives
- Model the LeetCode dataset as a **graph-based system**
- Identify **important problems and dominant topics**
- Analyze **relationships between algorithmic concepts**
- Detect **clusters representing problem-solving patterns**
- Determine a **minimal subset of problems** for maximum concept coverage
- Design **efficient learning strategies**

---

## 🗂️ Dataset
The dataset is collected by scraping the LeetCode problem set.

### Each problem contains:
- Problem ID  
- Title  
- Difficulty (Easy / Medium / Hard)  
- Topic Tags  

---

## 🧠 Network Models

### 🔹 Problem–Tag Bipartite Graph
- Nodes: Problems and Tags  
- Edge: A problem is associated with a tag  

---

### 🔹 Tag–Tag Network
- Nodes: Tags  
- Edge: Tags co-occur in the same problem  
- Captures **concept relationships**

---

## 📈 Analysis Techniques

- **Degree Centrality** → Identifies dominant tags and multi-concept problems  
- **Betweenness Centrality** → Detects bridge problems and connector tags  
- **Eigenvector Centrality** → Measures global influence  
- **Community Detection (Louvain)** → Finds clusters of related concepts  
- **Clustering Coefficient** → Analyzes redundancy  
- **Greedy Set Cover** → Finds minimal problem subset  

---

## 🔍 Key Findings

### 🔹 Hub Tags Dominate
A small number of tags such as **Array, Hash Table, String, and Dynamic Programming** connect a large portion of the problem space.

---

### 🔹 Difficulty Reflects Conceptual Breadth
- Easy → ~2 tags  
- Medium → ~3 tags  
- Hard → ~4 tags  

Hard problems involve **more interconnected concepts**.

---

### 🔹 High Redundancy in Dataset
Only **26 problems** are sufficient to cover all **72 tags**, with the first few problems contributing nearly half of the total coverage.

---

### 🔹 Community Structure
The network forms distinct clusters representing:
- Graph algorithms  
- Dynamic Programming  
- String processing  
- Mathematical reasoning  
- Data structures  

---

### 🔹 Structural Separation
Database (SQL) problems form an **independent subgraph**, separate from algorithmic problem domains.

---

## 📊 Visualizations
- Network graphs and layouts generated using **Gephi**
- Statistical plots generated using Python libraries

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NetworkX  
- Selenium  
- Gephi  

---

## ⚠️ Limitations
- Static snapshot of dataset  
- Tag quality depends on manual labeling  
- Problem–problem network not fully analyzed due to scale  
- Greedy set cover provides approximate solution  

---

## 🔮 Future Scope
- Scalable analysis of large problem–problem networks  
- Personalized learning path recommendation  
- Integration of user performance data  
- Dynamic tracking of network evolution  
- Code-level similarity analysis  

---

## 👨‍💻 Authors
- G Bhanu Prakash  
- K Aditya  
- B Hari Charan Goud  
- K Nithin  
- Y Suchethan Reddy  

---

## ⭐ Final Insight
> The structure of the LeetCode problem space is highly interconnected, where a small number of core concepts and problems dominate learning efficiency, enabling strategic and optimized preparation.
