import uuid

class TetrisBlock:
    def __init__(self, content, block_type="data_core"):
        self.id = str(uuid.uuid4())
        self.content = content
        self.type = block_type
        self.fitness = 0.0
        self.generation = 0
        self.block_id = self.id
    
    def to_dict(self):
        return {
            "block_id": self.id,
            "content": self.content,
            "type": self.type,
            "fitness": self.fitness,
            "generation": self.generation
        }
