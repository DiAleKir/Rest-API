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

class PayloadsNegative:

    cpu = ["M1", "M2", "M3", f"Intel Core i{random.randint(7,9)}"]
    hard_disk = ["1 TB", "2 TB", "500 MB"]

    empty_body = {}
    empty_name = {
        "data": {
            "year": random.randint(2015,2025),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    invalid_name = {
        "name": random.choice([1232, "+-$@&^!", " "]),
        "data": {
            "year": random.randint(2015, 2025),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    body_without_data = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}"
    }
    data_without_price = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    negative_price = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": -133,
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    price_is_0 = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": 0,
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    invalid_price = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": random.choice(["string", "+-$@&^!", " "]),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    year_is_0 = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": 0,
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    negative_year = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": -158,
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    invalid_year = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.choice(["string", "+-$@&^!", " "]),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice(hard_disk)
        }
    }
    invalid_cpu = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": random.randint(1500, 3000),
            "CPU model": random.choice([178, "+-$@&^!", "", " "]),
            "Hard disk size": random.choice(hard_disk)
        }
    }
    invalid_hard_disk = {
        "name": f"Apple MacBook Pro {random.randint(14, 18)}",
        "data": {
            "year": random.randint(2015, 2025),
            "price": random.randint(1500, 3000),
            "CPU model": f"Intel Core {random.choice(cpu)}",
            "Hard disk size": random.choice([158, "+-$@&^!", "", " "])
        }
    }
