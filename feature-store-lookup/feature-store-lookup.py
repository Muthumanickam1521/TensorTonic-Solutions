def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """

    output = []

    for request in requests:
        usr = request.get("user_id")
        usr_feat = request.get("online_features")

        offline_feat = feature_store.get(usr, None)

        if offline_feat is None:
            offline_feat = defaults

        output.append({**usr_feat, **offline_feat})

    return output
