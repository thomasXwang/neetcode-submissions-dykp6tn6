class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        
        x = init

        for i in range(iterations):
            grad_x = 2*x
            x -= learning_rate * grad_x

        return round(x, 5)