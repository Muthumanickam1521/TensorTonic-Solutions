def split_timestamp(tsmp):
    tsmp_parts = tsmp.split("-")
    return int(tsmp_parts[0]), int(tsmp_parts[1]), int(tsmp_parts[2])


def promote_model(models):
    """
    Decide which model version to promote to production.
    """

    if len(models) == 0:
        return ""

    elif len(models) == 1:
        return models[0]["name"]

    models_sorted = sorted(models, key=lambda x: x["accuracy"], reverse=True)
    
    promoted_model = models_sorted[0]
    model = models_sorted[1]


    acc = model["accuracy"]
    pacc = promoted_model["accuracy"]
    
    pname = promoted_model["name"]
    name = model["name"]

    if pacc < acc:
        return name

    elif pacc == acc:
        platency = promoted_model["latency"]
        latency = model["latency"]

        if platency > latency:
            return name

        elif platency == latency:
            ptimestamp = promoted_model["timestamp"]
            timestamp = model["timestamp"]
            pyr, pm, pd = split_timestamp(ptimestamp)
            yr, m, d = split_timestamp(timestamp)

            if yr > pyr:
                return name
            elif (yr == pyr) and (m > pm):
                return name
            elif (yr == pyr) and (m == pm) and (d > pd):
                return name

    return pname
