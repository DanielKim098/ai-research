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

class AbstractEvolutionTracker(EvolutionPathTracker):
    """
    Enhanced evolution tracker using symbolic representation for abstract potential.
    """
    def __init__(self):
        super().__init__()
        self.potential_symbol = "Δ" # 델타 기호 사용

    def identify_potential(self, step_description):
        """
        Identifies if a step description has abstract potential using keywords.
        """
        if "complex" in step_description.lower() or "adaptive" in step_description.lower() or "synergy" in step_description.lower():
            return f"{step_description} {self.potential_symbol}"
        return step_description
    def add_step(self, step_description):
        """
        Overrides add_step to incorporate potential identification.
        """
        self.evolution_steps.append(self.identify_potential(step_description))



# Example usage
tracker = AbstractEvolutionTracker()
tracker.add_step("Initial safety alignment established.")
tracker.add_step("Achieved complex resource optimization.")
tracker.add_step("Enabled adaptive synergy with human")
tracker.display_path()
