def apply_discount_to_cart(user, discount, cart_total):
    """
    Applique une réduction sur le montant total du panier si les conditions sont remplies.
    
    :param user: Objet utilisateur
    :param discount: Objet discount
    :param cart_total: Montant total du panier
    :return: Nouveau montant du panier après application de la réduction
    """
    # Vérifiez si l'utilisateur est actif
    if not user.is_active:
        raise ValueError("L'utilisateur n'est pas actif")

    # Vérifiez si l'utilisateur a atteint le nombre maximum de promotions utilisées
    if user.max_number_discount and user.nb_discount_used >= user.max_number_discount:
        raise ValueError("L'utilisateur a atteint le nombre maximum de promotions utilisées")

    # Vérifiez que le montant du panier atteint le minimum requis pour la réduction
    if discount.minimum_cart and cart_total < discount.minimum_cart:
        raise ValueError(f"Le montant du panier doit être au moins de {discount.minimum_cart} pour appliquer la réduction")

    # Appliquez la réduction (par exemple, réduction en pourcentage ou montant fixe)
    if discount.is_percentage:
        discount_amount = cart_total * (discount.amount / 100)
    else:
        discount_amount = discount.amount

    # Assurez-vous que la réduction ne dépasse pas le montant total du panier
    discount_amount = min(discount_amount, cart_total)

    # Calcul du nouveau montant du panier après réduction
    new_cart_total = cart_total - discount_amount

    # Mettre à jour le nombre de promotions utilisées par l'utilisateur
    user.nb_discount_used += 1
    user.save()

    return new_cart_total
