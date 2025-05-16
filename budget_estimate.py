import matplotlib.pyplot as plt

categories = [
    "LinkedIn Sales Navigator",
    "Content Creation",
    "Integration Development",
    "Social Media Tools",
    "Gamification Development",
    "Broadbean Subscription",
    "Influencer Fees"
]
costs = [600, 3000, 5000, 300, 2000, 3000, 4000]

plt.figure(figsize=(10, 6))
bars = plt.barh(categories, costs, color='skyblue')
plt.xlabel('Cost ($)')
plt.title('Budget Estimate Breakdown')

for bar in bars:
    plt.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
             f"${bar.get_width():,}", va='center')

plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
