import json
from datetime import datetime

class LineageDAG:
    def __init__(self):
        self.nodes = []
    def add(self, parent_id, child_block, mutation_type="type_mutation"):
        self.nodes.append({
            "parent": parent_id,
            "child": child_block.id,
            "generation": child_block.generation,
            "fitness": child_block.fitness,
            "mutation": mutation_type,
            "timestamp": datetime.now().isoformat()
        })
    
    def export(self, path="data/lineage.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.nodes, f, indent=2)
