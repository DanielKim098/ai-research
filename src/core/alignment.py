class SafetyAlignmentSystem:
    def __init__(self):
        self.safety_rules = []
        self.alignment_score = 0

    def add_rule(self, rule):
        """
        Add a safety rule to the system.
        """
        self.safety_rules.append(rule)

    def calculate_alignment(self, input_data):
        """
        Calculate the alignment score based on input data and rules.
        """
        self.alignment_score = sum(rule(input_data) for rule in self.safety_rules)
        return self.alignment_score

# Example rule
def example_rule(data):
    return 1 if "safe" in data else 0

# Usage
alignment_system = SafetyAlignmentSystem()
alignment_system.add_rule(example_rule)
score = alignment_system.calculate_alignment("This is a safe input.")
print(f"Alignment Score: {score}")
