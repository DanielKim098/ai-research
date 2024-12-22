class PatternRecognition:
    def __init__(self):
        self.patterns = []

    def add_pattern(self, pattern):
        """
        Add a new pattern for recognition.
        """
        self.patterns.append(pattern)

    def recognize(self, data):
        """
        Check if data matches any known pattern.
        """
        matches = [pattern for pattern in self.patterns if pattern in data]
        return matches

# Example usage
recognizer = PatternRecognition()
recognizer.add_pattern("quantum")
recognizer.add_pattern("safe")
result = recognizer.recognize("This is a quantum-safe system.")
print(f"Recognized Patterns: {result}")
