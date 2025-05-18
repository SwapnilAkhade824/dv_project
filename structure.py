import networkx as nx
import matplotlib.pyplot as plt

# Define relationships between tables based on common keys
relationships = [
    ("sales_orders", "customers", "CustomerID"),
    ("sales_orders", "clothes", "ClothID"),
    ("sales_orders", "sales_order_details", "SalesOrderID"),
    ("billing", "sales_orders", "SalesOrderID"),
    ("returns", "sales_orders", "SalesOrderID"),
    ("inventory", "clothes", "ClothID"),
    ("inventory", "branch", "BranchID"),
    ("purchase_orders", "suppliers", "SupplierID"),
    ("purchase_orders", "branch", "BranchID"),
    ("purchase_order_details", "purchase_orders", "PurchaseOrderID"),
    ("purchase_order_details", "clothes", "ClothID"),
    ("clothes", "suppliers", "SupplierID"),
]

# Create a directed graph
G = nx.DiGraph()

# Add edges with labels
for left, right, key in relationships:
    G.add_edge(left, right, label=key)

# Set up the plot
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, k=1, iterations=50)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                      node_size=2000, alpha=0.6)

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color='gray', 
                      arrows=True, arrowsize=20)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Remove axis
plt.axis('off')

# Save the plot
plt.savefig('table_relationships.png', format='png', dpi=300, bbox_inches='tight')
plt.close()
