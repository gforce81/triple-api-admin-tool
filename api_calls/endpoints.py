endpoints = {
    "base_urls": {
        "dev": {
            "base_url": "https://api.partners.dev.tripleupdev.com",
            "auth_url": "https://auth.partners.dev.tripleupdev.com/oauth2/token",
            "ui_base_url": "https://ui-api.partners.dev.tripleupdev.com"
        },
        "sandbox": {
            "base_url": "https://api.sandbox.tripleup.dev",
            "auth_url": "https://auth.sandbox.tripleup.dev/oauth2/token",
            "ui_base_url": "https://ui-api.partners.sandbox.tripleup.dev"
        },
        "prod": {
            "base_url": "https://api.tripleup.dev",
            "auth_url": "https://auth.tripleup.dev/oauth2/token",
            "ui_base_url": "https://ui-api.tripleup.dev"
        },
        "qa": {
            "base_url": "https://api.partners.qa.tripleupdev.com",
            "auth_url": "https://auth.qa.tripleup.dev/oauth2/token",
            "ui_base_url": "https://ui-api.partners.qa.tripleupdev.com"
        }
    },
    "card_accounts": {
        "POST_getCardAccountExternal": "/partner/card-account.by-ids",
        "GET_listCardAccounts": "/partner/card-accounts",
        "POST_createCardAccount": "/partner/card-accounts",
        "GET_getCardAccount": "/partner/card-accounts/{cardholder_id}",
        "PATCH_updateCardAccount": "/partner/card-accounts/{cardholder_id}"
    },
    "card_programs": {
        "GET_listCardPrograms": "/partner/card-programs",
        "POST_createCardProgram": "/partner/card-programs",
        "GET_getCardProgram": "/partner/card-programs/{card_program_id}",
        "PATCH_updateCardProgram": "/partner/card-programs/{card_program_id}"
    },
    "offer_activation": {
        "PUT_activateOffer": "/partner/card-accounts/{cardholder_id}/offers/activation/id/{offer_id}"
    },
    "offer_display": {
        "GET_activatedOffers": "/partner/card-accounts/{cardholder_id}/offers/activation",
        "GET_offersCategories": "/partner/card-accounts/{cardholder_id}/offers/categories",
        "POST_getOffersRecommendations": "/partner/card-accounts/{cardholder_id}/offers.recommendations",
        "POST_searchOffers": "/partner/card-accounts/{cardholder_id}/offers.search",
        "GET_offersDetailsByCardholder": "/partner/card-accounts/{cardholder_id}/offers.details",
        "GET_offersDetails": "/partner/offers/{offer_id}/details"
    },
    "offer_filters": {
        "GET_getFilter": "/partner/offer-filters/{filter_id}",
        "PATCH_updateFilter": "/partner/offer-filters/{filter_id}",
        "DEL_deleteFilter": "/partner/offer-filters/{filter_id}",
        "GET_listFilters": "/partner/offer-filters",
        "POST_createFilter": "/partner/offer-filters"
    },
    "offer_providers": {
        "GET_listMerchants": "/partner/merchants",
        "POST_createMerchant": "/partner/merchants",
        "GET_getMerchant": "/partner/merchants/{merchant_id}",
        "PATCH_updateMerchant": "/partner/merchants/{merchant_id}",
        "GET_listMerchantLocations": "/partner/merchant-locations",
        "POST_createMerchantLocation": "/partner/merchant-locations",
        "GET_merchantLocation": "/partner/merchant-locations/{merchant_location_id}",
        "PATCH_merchantLocation": "/partner/merchant-locations/{merchant_location_id}",
        "DEL_merchantLocation": "/partner/merchant-locations/{merchant_location_id}",
        "GET_listOffers": "/partner/offers",
        "POST_createOffers": "/partner/offers",
        "PATCH_updateOffers": "/partner/offers/{offer_id}"

    },
    "portfolio_management": {
        "GET_listPublishers": "/partner/publishers",
        "POST_createPublisher": "/partner/publishers",
        "GET_getPublisher": "/partner/publishers/{publisher_id}",
        "PATCH_updatePublisher": "/partner/publishers/{publisher_id}"
    },
    "rewards": {
        "GET_listRewards": "/partner/rewards",
        "PATCH_updateReward": "/partner/rewards/{reward_id}",
        "GET_getReward": "/partner/rewards/{reward_id}"
    },
    "transactions": {
        "GET_listTransactions": "/partner/transactions",
        "GET_getTransaction": "/partner/transactions/{transaction_id}",
        "POST_createTransaction": "/partner/transactions"
    },
    "user_events": {
        "POST_userEvent": "/partner/user-events"
    },
    "ui-api": {
        "POST_initiateSession": "/initiate-session",
        "POST_offersHome": "/offers-home"
    }
}

