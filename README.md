# Analysis of Algorithms - Project 1

**Algorithmic Optimization in Cloud Computing**  
*Two Fundamental Algorithmic Paradigms Applied to Real-World Problems*

---

## **Project Structure**

```
Project Root
├── vm_scheduler_implementation.py            # Greedy Algorithm Implementation
├── datacenter_proximity_implementation.py    # Divide & Conquer Implementation
├── generate_graphs.py                        # Visualization Generation
├── test_project.py                           # Integration Tests
├── README.md                                 # Project Documentation
└── experimental_results/                     # Generated Visualizations
    ├── VM_performance_dashboard.png          # VM Scheduler Performance
    ├── VM_realistic_scenario_timeline.png    # Scheduling Timeline
    ├── datacenter_performance_dashboard.png  # Datacenter Analysis
    └── datacenter_map_analysis.png           # Global Datacenter Map
```

---

## **Problems Solved**

### **Problem 1: VM Reservation Scheduling (Greedy Algorithm)**

- **Real-World Context**: Cloud provider optimizing customer VM reservations
- **Technical Problem**: Interval scheduling with overlapping time windows
- **Algorithm**: Greedy "earliest finish time" strategy
- **Complexity**: O(n log n) time, O(1) space
- **Business Impact**: Maximizes customer satisfaction and resource utilization

### **Problem 2: Datacenter Proximity Analysis (Divide & Conquer)**

- **Real-World Context**: Network optimization for global cloud infrastructure
- **Technical Problem**: Closest pair of points in 2D space
- **Algorithm**: Divide & conquer with geometric optimization
- **Complexity**: O(n log n) time vs O(n²) brute force
- **Business Impact**: Enables efficient routing and disaster recovery planning

---

## **How to Run the Project**

### **Prerequisites**

```bash
# Install required Python packages
pip install matplotlib numpy
```

### **1. Test VM Scheduler (Greedy Algorithm)**

```bash
python vm_scheduler_implementation.py
```

**What it does:**

- Demonstrates VM reservation scheduling on 18 realistic jobs
- Shows greedy algorithm selecting optimal non-overlapping reservations
- Validates O(n log n) complexity experimentally
- Reports success rate and performance metrics

### **2. Test Datacenter Proximity (Divide & Conquer)**

```bash
python datacenter_proximity_implementation.py
```

**What it does:**

- Analyzes 18 real global datacenter locations
- Finds closest pair using divide & conquer algorithm
- Compares performance against brute force approach
- Validates O(n log n) vs O(n²) complexity difference

### **3. Generate All Visualizations**

```bash
python generate_graphs.py
```

**What it creates:**

- Performance dashboards for both algorithms
- Complexity validation graphs
- Realistic scenario timelines
- Global datacenter proximity maps
- All outputs saved to `experimental_results/` directory

### **4. Run Complete Integration Test**

```bash
python test_project.py
```

**What it verifies:**

- Both algorithms work correctly
- No overlapping intervals in greedy solution
- Divide & conquer matches brute force results
- Graph generation functions are available
- Project is ready for submission

---

## **Key Results**

| Algorithm | Problem | Time Complexity | Experimental R² | Performance |
|-----------|---------|-----------------|-----------------|-------------|
| **Greedy** | VM Scheduling | O(n log n) | 0.98+ | 44.4% success rate |
| **Divide & Conquer** | Datacenter Proximity | O(n log n) | 0.95+ | 9× fewer comparisons |

### **VM Scheduler Results:**

- **Input**: 18 overlapping VM reservation requests
- **Output**: 8 optimal non-overlapping reservations selected
- **Success Rate**: 44.4% (significant improvement over random selection)
- **Verification**: Zero overlaps in final solution

### **Datacenter Proximity Results:**

- **Input**: 18 global datacenter coordinates
- **Closest Pair**: AWS-US-East-1 and Azure-East-US (both in Virginia)
- **Distance**: 0.4912 degrees
- **Performance**: Divide & conquer uses 9× fewer comparisons than brute force

---

## **Technical Implementation**

### **Greedy Algorithm Features:**

- Optimal interval scheduling implementation
- Real VM reservation data model
- Performance measurement and complexity validation
- Business scenario demonstration
- Correctness verification (no overlaps)

### **Divide & Conquer Features:**

- Geometric closest pair algorithm
- 7-point optimization for strip processing
- Brute force comparison for validation
- Real datacenter coordinate data
- Performance scaling analysis

### **Visualization Features:**

- Scalability analysis (log-log plots)
- Algorithm comparison charts
- Realistic scenario timelines
- Global datacenter maps
- Complexity validation graphs

---

## **Experimental Validation**

Both algorithms demonstrate strong correlation with theoretical complexity:

- **VM Scheduler**: R² ≈ 0.98 correlation with O(n log n)
- **Datacenter Analysis**: R² ≈ 0.95 correlation with O(n log n)
- **Brute Force**: R² = 1.00 correlation with O(n²)

Performance testing validates theoretical predictions across input sizes from 10 to 5000 elements.

---
