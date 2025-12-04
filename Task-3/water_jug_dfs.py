class WaterJugDFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()
        self.solution_path = []
        
    def is_goal(self, state):
        jug1, jug2 = state
        return jug1 == self.target or jug2 == self.target
    
    def get_next_states(self, state):
        jug1, jug2 = state
        next_states = []
        
        if jug1 < self.jug1_capacity:
            next_states.append(
                ((self.jug1_capacity, jug2), 
                 f"Fill Jug 1: ({jug1}, {jug2}) -> ({self.jug1_capacity}, {jug2})")
            )
        
        if jug2 < self.jug2_capacity:
            next_states.append(
                ((jug1, self.jug2_capacity), 
                 f"Fill Jug 2: ({jug1}, {jug2}) -> ({jug1}, {self.jug2_capacity})")
            )
        
        if jug1 > 0:
            next_states.append(
                ((0, jug2), 
                 f"Empty Jug 1: ({jug1}, {jug2}) -> (0, {jug2})")
            )
        
        if jug2 > 0:
            next_states.append(
                ((jug1, 0), 
                 f"Empty Jug 2: ({jug1}, {jug2}) -> ({jug1}, 0)")
            )
        
        if jug1 > 0 and jug2 < self.jug2_capacity:
            pour_amount = min(jug1, self.jug2_capacity - jug2)
            new_jug1 = jug1 - pour_amount
            new_jug2 = jug2 + pour_amount
            next_states.append(
                ((new_jug1, new_jug2), 
                 f"Pour Jug 1 -> Jug 2: ({jug1}, {jug2}) -> ({new_jug1}, {new_jug2})")
            )
        
        if jug2 > 0 and jug1 < self.jug1_capacity:
            pour_amount = min(jug2, self.jug1_capacity - jug1)
            new_jug1 = jug1 + pour_amount
            new_jug2 = jug2 - pour_amount
            next_states.append(
                ((new_jug1, new_jug2), 
                 f"Pour Jug 2 -> Jug 1: ({jug1}, {jug2}) -> ({new_jug1}, {new_jug2})")
            )
        
        return next_states
    
    def dfs(self, state, path):
        if self.is_goal(state):
            self.solution_path = path
            return True
        
        self.visited.add(state)
        
        for next_state, rule in self.get_next_states(state):
            if next_state not in self.visited:
                if self.dfs(next_state, path + [(next_state, rule)]):
                    return True
        
        return False
    
    def solve(self):
        initial_state = (0, 0)
        
        print(f"\n{'='*70}")
        print(f"Water Jug Problem - DFS Solution")
        print(f"{'='*70}")
        print(f"Jug 1 Capacity: {self.jug1_capacity} liters")
        print(f"Jug 2 Capacity: {self.jug2_capacity} liters")
        print(f"Target Amount: {self.target} liters")
        print(f"{'='*70}\n")
        
        if self.dfs(initial_state, []):
            print(f"✓ Solution Found! ({len(self.solution_path)} steps)\n")
            print(f"Initial State: (0, 0)")
            print(f"{'-'*70}")
            
            for i, (state, rule) in enumerate(self.solution_path, 1):
                print(f"Step {i}: {rule}")
            
            print(f"{'-'*70}")
            final_state = self.solution_path[-1][0]
            print(f"Final State: {final_state}")
            print(f"\n✓ Target of {self.target} liters achieved!")
            print(f"{'='*70}\n")
            
            return self.solution_path
        else:
            print(f"✗ No solution found!")
            print(f"{'='*70}\n")
            return None



print("\n" + "="*70)
print("EXAMPLE 1: Classic Water Jug Problem (4L, 3L, Target: 2L)")
print("="*70)
wj1 = WaterJugDFS(jug1_capacity=4, jug2_capacity=3, target=2)
wj1.solve()

print("\n" + "="*70)
print("EXAMPLE 2: 5-3 Water Jug Problem (5L, 3L, Target: 4L)")
print("="*70)
wj2 = WaterJugDFS(jug1_capacity=5, jug2_capacity=3, target=4)
wj2.solve()

print("\n" + "="*70)
print("EXAMPLE 3: Custom Water Jug Problem (7L, 5L, Target: 6L)")
print("="*70)
wj3 = WaterJugDFS(jug1_capacity=7, jug2_capacity=5, target=6)
wj3.solve()

