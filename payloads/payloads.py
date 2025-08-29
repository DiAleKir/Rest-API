import random


class Payloads:

    cpu = ["M1", "M2", "M3", f"Intel Core i{random.randint(7,9)}"]
    hard_disk = ["1 TB", "2 TB", "500 MB"]

    new_object = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015,2025),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }

    update_object = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk),
            "color": "Black"
        }
    }

    patch_object = [
        {
            "name": f"Apple MacBook Pro {random.randint(14, 18)}"
        },
        {
            "data": {
                "year": random.randint(2015, 2025),
                "price": random.randint(1500, 3000),
                "CPU model": f"Intel Core {random.choice(cpu)}",
                "Hard disk size": random.choice(hard_disk),
                "color": "Silver"
            }
        }
    ]
