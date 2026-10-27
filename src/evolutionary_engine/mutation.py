# Iz valery_dynamic_mutation_report_data.csv - 56 runova

def dynamic_mutation_rate(block_type, base=0.12):
    technical = ["bios","ssd","diskpart","uefi","boot","mbr","gpt","rufus","data_core"]
    emotional = ["energija","povjerenje","podrška","zajedno","vječno","identitet","Identitet"]
    if any(t in block_type for t in technical):
        return 0.05  # best 0.714
    elif any(e in block_type for e in emotional):
        return 0.30  # best 0.957
    elif "ethical" in block_type or "Evolucija" in block_type:
        return 0.80  # best 0.969
    return base
