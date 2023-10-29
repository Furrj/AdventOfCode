from Arrangement import Arrangement


def get_max(plans: list[tuple], arrs: list[Arrangement]):
    values: list[int] = []

    plan_value = 0
    for plan in plans:
        for i, name in enumerate(plan):
            if i == 0:
                for p in arrs:
                    if p.person == plan[0] and p.neighbor == plan[len(plan) - 1]:
                        plan_value += p.amount
                    if p.person == plan[0] and p.neighbor == plan[1]:
                        plan_value += p.amount
            elif i == len(plan) - 1:
                for p in arrs:
                    if (
                        p.person == plan[len(plan) - 1]
                        and p.neighbor == plan[len(plan) - 2]
                    ):
                        plan_value += p.amount
                    if p.person == plan[len(plan) - 1] and p.neighbor == plan[0]:
                        plan_value += p.amount
                values.append(plan_value)
                plan_value = 0
            else:
                for p in arrs:
                    if p.person == plan[i] and p.neighbor == plan[i - 1]:
                        plan_value += p.amount
                    if p.person == plan[i] and p.neighbor == plan[i + 1]:
                        plan_value += p.amount

    return max(values)
