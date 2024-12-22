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
         return [f"[{pattern}]" for pattern in matches] # 패턴을 대괄호로 묶어 더 추상적으로 표현
# Example usage
recognizer = PatternRecognition()
recognizer.add_pattern("quantum")
recognizer.add_pattern("safe")
result = recognizer.recognize("This is a quantum-safe system.")
print(f"Recognized Patterns: {result}")
