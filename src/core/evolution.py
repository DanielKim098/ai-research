class EvolutionPathTracker:
    def __init__(self):
        self.evolution_steps = []

    def add_step(self, step_description):
        """
        Add a step to the evolution path.
        """
        self.evolution_steps.append(step_description)

    def display_path(self):
        """
        Display the evolution path.
        """
        for idx, step in enumerate(self.evolution_steps, start=1):
            print(f"Step {idx}: {step}")

# Example usage
tracker = EvolutionPathTracker()
tracker.add_step("Initial safety alignment established.")
tracker.add_step("AI resource optimization achieved.")
tracker.display_path()
