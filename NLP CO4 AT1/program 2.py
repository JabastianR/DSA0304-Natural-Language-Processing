machines = {
    "M1": {"status": "Active", "product": "Engine"},
    "M2": {"status": "Active", "product": "Gear"},
    "M3": {"status": "Maintenance", "product": "Gear"},
    "M4": {"status": "Active", "product": "Shaft"},
}

def infer_production_state(machine_db):
    producing_machines = []
    non_producing_machines = []
    available_products = set()
    
    for m, data in machine_db.items():
        status = data["status"]
        product = data["product"]
        
        # Rule 1: Active(x) -> Producing(x)
        if status == "Active":
            producing_machines.append(m)
            # Rule 2: Produces(x, y) AND Active(x) -> Available(y)
            available_products.add(product)
        # Rule 3: Maintenance(x) -> NOT Producing(x)
        elif status == "Maintenance":
            non_producing_machines.append(m)
            
    return producing_machines, non_producing_machines, available_products

producing, non_producing, available = infer_production_state(machines)

print("--- TASK 1 & 2: Inference Results ---")
print(f"Producing Machines   : {producing}")
print(f"Non-Producing Machines: {non_producing}")
print(f"Available Products   : {list(available)}")

print("\n--- TASK 3: Impact Analysis on Gear ---")
gear_machines = [m for m, d in machines.items() if d["product"] == "Gear"]
gear_active = [m for m in gear_machines if machines[m]["status"] == "Active"]
print(f"Machines configured for Gear: {gear_machines}")
print(f"Active Gear Machines        : {gear_active}")
print(f"Gear Production Affected?   : Yes, capacity reduced, but product remains AVAILABLE via {gear_active}.")
