def dynamic_mutation_rate(block_type, base=0.12):
    technical = ["bios","ssd","diskpart","uefi","boot","mbr","gpt","rufus","data_core"]
    emotional = ["energija","povjerenje","podrška","zajedno","vječno","identitet"]
    if any(t in block_type for t in technical):
        return 0.05
    elif any(e in block_type for e in emotional):
        return 0.30
    elif "ethical" in block_type:
        return 0.80
    return base
