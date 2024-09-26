def ask_question(question):
    print(question)
    answer = input().lower()
    return answer

def classify_mbti():
    questions = [
        "Do you tend to focus on the outer world? (yes/no)",
        "Do you often think about the future or possibilities? (yes/no)",
        "Do you tend to make decisions based on logic and reason rather than emotions? (yes/no)",
        "Do you prefer to have things decided or settled? (yes/no)",
        "Do you enjoy social gatherings and interacting with people? (yes/no)",
        "Are you more comfortable with facts and concrete information than theories? (yes/no)",
        "Do you find it easy to express your feelings openly? (yes/no)",
        "Do you prefer to follow a plan rather than being spontaneous? (yes/no)",
        "Do you enjoy exploring new ideas and concepts? (yes/no)",
        "Are you usually the one to initiate conversations in social settings? (yes/no)",
        "Do you prefer to work in a structured and organized environment? (yes/no)",
        "Are you more focused on the present moment than the future? (yes/no)",
        "Do you value harmony and avoid conflict? (yes/no)",
        "Do you trust your intuition when making decisions? (yes/no)",
        "Are you energized by spending time alone? (yes/no)",
        "Do you prefer to keep your options open rather than making a final decision? (yes/no)"
    ]

    mbti_type = ""
    for question in questions:
        answer = ask_question(question)
        if answer == "yes":
            mbti_type += "E" if "extrovert" in question.lower() else "I"
            mbti_type += "N" if "intuition" in question.lower() else "S"
            mbti_type += "F" if "feelings" in question.lower() else "T"
            mbti_type += "J" if "judging" in question.lower() else "P"
        else:
            mbti_type += "I" if "introvert" in question.lower() else "E"
            mbti_type += "S" if "sensing" in question.lower() else "N"
            mbti_type += "T" if "thinking" in question.lower() else "F"
            mbti_type += "P" if "perceiving" in question.lower() else "J"

    return mbti_type


def classify_body_type():
    questions = [
        "Are you generally slender and have difficulty gaining weight? (yes/no)",
        "Do you tend to gain weight easily and have a rounder body shape? (yes/no)",
        "Do you have a naturally muscular and athletic build? (yes/no)",
        "Would you describe your body shape as pear-shaped? (yes/no)",
        "Do you have a broad chest and narrow waist? (yes/no)",
        "Would you say you have a stocky or sturdy build? (yes/no)",
        "Is your body shape more hourglass-like with defined curves? (yes/no)"
    ]

    body_types = {
        "Slender": ["slender", "ectomorph", "lean"],
        "Endomorph": ["round", "rounder", "pear-shaped"],
        "Mesomorph": ["muscular", "athletic", "broad", "sturdy", "hourglass"]
    }

    for question in questions:
        answer = ask_question(question)
        if answer == "yes":
            for body_type, keywords in body_types.items():
                for keyword in keywords:
                    if keyword in question.lower():
                        return body_type.capitalize()
                        break

    return "Undetermined"


def classify_body_language():
    questions = [
        "Do you often use hand gestures while speaking? (yes/no)",
        "Do you prefer to listen carefully to others without interrupting? (yes/no)",
        "Do you enjoy physical touch as a form of communication? (yes/no)",
        "Do you maintain eye contact during conversations? (yes/no)",
        "Are you comfortable with close physical proximity when communicating? (yes/no)",
        "Do you tend to fidget or move around when sitting for a long time? (yes/no)",
        "Are your facial expressions usually easy to read? (yes/no)"
    ]

    body_language = ""
    for question in questions:
        answer = ask_question(question)
        if answer == "yes":
            body_language = question.split()[3].capitalize()
            break

    return body_language


def personalized_clothing_recommendations(mbti_type, body_type, body_language):
    recommendations = {
    "INTJ": {
        "Clothing": "Sleek and professional attire",
        "Colors": "Dark colors such as black, navy, and charcoal gray",
        "Fit": "Tailored and structured",
        "Textures and Fabrics": "Smooth and high-quality fabrics",
        "Accessories": "Minimalist and functional accessories",
        "Hair and Makeup": "Neat and polished hairstyle, subtle makeup",
        "Footwear": "Classic and comfortable shoes",
        "Layering": "Layer with tailored jackets or cardigans",
        "Personal Touches": "Add a statement watch or elegant jewelry",
        "Confidence": "Confidence comes from feeling put-together and prepared"
    },
     "INTP": {
        "Clothing": "Casual and comfortable attire with a touch of quirkiness",
        "Colors": "Muted tones and earthy colors",
        "Fit": "Relaxed and loose-fitting",
        "Textures and Fabrics": "Natural and breathable fabrics",
        "Accessories": "Unique and eccentric accessories",
        "Hair and Makeup": "Messy or tousled hairstyle, natural makeup",
        "Footwear": "Casual sneakers or comfortable boots",
        "Layering": "Layer with lightweight sweaters or flannels",
        "Personal Touches": "Express your creativity through accessories or prints",
        "Confidence": "Confidence comes from embracing your individuality"
    },
    "ENTJ": {
        "Clothing": "Power suits and structured outfits",
        "Colors": "Bold and authoritative colors such as navy, gray, and burgundy",
        "Fit": "Sharp and tailored",
        "Textures and Fabrics": "Luxurious and high-quality fabrics",
        "Accessories": "Statement accessories to command attention",
        "Hair and Makeup": "Neat hairstyle, bold makeup for impact",
        "Footwear": "Polished dress shoes or boots",
        "Layering": "Layer with structured blazers or coats",
        "Personal Touches": "Wear a quality watch or unique tie clip",
        "Confidence": "Confidence comes from leading by example and being decisive"
    },
    "ENTP": {
        "Clothing": "Versatile and trendy pieces",
        "Colors": "Mix of bold and neutral colors",
        "Fit": "Modern and tailored",
        "Textures and Fabrics": "Experiment with different textures and fabrics",
        "Accessories": "Statement accessories to showcase personality",
        "Hair and Makeup": "Edgy hairstyles and bold makeup looks",
        "Footwear": "Fashion-forward shoes with unique details",
        "Layering": "Layer with unexpected combinations and patterns",
        "Personal Touches": "Incorporate quirky or unconventional elements",
        "Confidence": "Confidence comes from embracing creativity and spontaneity"
    },
    "INFJ": {
        "Clothing": "Bohemian and ethereal attire",
        "Colors": "Soft and muted tones, earthy colors",
        "Fit": "Flowy and loose-fitting",
        "Textures and Fabrics": "Natural and breathable fabrics",
        "Accessories": "Vintage-inspired and unique accessories",
        "Hair and Makeup": "Soft waves or braids, natural makeup with a hint of color",
        "Footwear": "Comfortable and stylish boots or sandals",
        "Layering": "Layer with lightweight scarves or shawls",
        "Personal Touches": "Express your creativity through handmade or customized items",
        "Confidence": "Confidence comes from embracing your unique perspective and values"
    },
    "INFP": {
        "Clothing": "Vintage-inspired and eclectic",
        "Colors": "Soft and pastel colors",
        "Fit": "Relaxed and comfortable",
        "Textures and Fabrics": "Natural and breathable fabrics",
        "Accessories": "Unique and whimsical accessories",
        "Hair and Makeup": "Messy or bohemian hairstyle, natural makeup",
        "Footwear": "Comfortable and whimsical footwear",
        "Layering": "Layer with lightweight and flowing fabrics",
        "Personal Touches": "Express your individuality through accessories or prints",
        "Confidence": "Confidence comes from embracing your uniqueness"
    },
    "ENFJ": {
        "Clothing": "Sophisticated and elegant",
        "Colors": "Warm and inviting colors",
        "Fit": "Flattering and feminine",
        "Textures and Fabrics": "Luxurious and soft fabrics",
        "Accessories": "Timeless and elegant accessories",
        "Hair and Makeup": "Polished hairstyle, classic makeup",
        "Footwear": "Stylish and comfortable heels or flats",
        "Layering": "Layer with chic blazers or statement coats",
        "Personal Touches": "Add a personal touch with delicate jewelry or scarves",
        "Confidence": "Confidence comes from connecting with others and being genuine"
    },
    "ENFP": {
        # Recommendations for ENFP
        "Clothing": "Eclectic and vibrant outfits with mix of patterns and bright colors",
        "Colors": "Bold and lively colors such as orange, yellow, and turquoise",
        "Fit": "Mix of loose and fitted styles for a fun and carefree look",
        "Textures and Fabrics": "Lightweight and breathable fabrics with playful prints",
        "Accessories": "Quirky and whimsical accessories to express individuality",
        "Hair and Makeup": "Fun and experimental hairstyles, colorful makeup looks",
        "Footwear": "Funky and unique shoes that make a statement",
        "Layering": "Layer with colorful scarves or statement jackets",
        "Personal Touches": "Express creativity through DIY or handmade accessories",
        "Confidence": "Confidence comes from embracing spontaneity and authenticity"
    },
    "ISTJ": {
        # Recommendations for ISTJ
        "Clothing": "Classic and timeless wardrobe staples",
        "Colors": "Neutral colors such as beige, gray, and navy",
        "Fit": "Clean and tailored silhouettes for a polished look",
        "Textures and Fabrics": "Sturdy and durable fabrics with minimal texture",
        "Accessories": "Simple and practical accessories that complement outfits",
        "Hair and Makeup": "Neat and conservative hairstyles, minimal makeup",
        "Footwear": "Comfortable and versatile shoes suitable for any occasion",
        "Layering": "Layer with classic blazers or structured cardigans",
        "Personal Touches": "Add subtle personal touches through monogrammed items or family heirlooms",
        "Confidence": "Confidence comes from being well-prepared and organized"
    },
    "ISFJ": {
        "Clothing": "Traditional and feminine styles",
        "Colors": "Soft and pastel colors",
        "Fit": "Modest and well-fitted",
        "Textures and Fabrics": "Soft and comfortable fabrics like cotton or silk",
        "Accessories": "Delicate and understated jewelry",
        "Hair and Makeup": "Neat and classic hairstyle, natural makeup",
        "Footwear": "Comfortable flats or low heels",
        "Layering": "Layer with cardigans or blazers",
        "Personal Touches": "Incorporate sentimental or meaningful accessories",
        "Confidence": "Confidence comes from feeling nurtured and supported"
    },
     "ESTJ": {
        "Clothing": "Sharp and tailored outfits",
        "Colors": "Bold and authoritative colors such as navy blue and burgundy",
        "Fit": "Fitted and structured",
        "Textures and Fabrics": "Durable and high-quality fabrics",
        "Accessories": "Classic and timeless accessories",
        "Hair and Makeup": "Neat and polished hairstyle, natural makeup",
        "Footwear": "Smart and practical shoes",
        "Layering": "Layer with vests or blazers for a polished look",
        "Personal Touches": "Add a sleek watch or professional bag",
        "Confidence": "Confidence comes from being well-prepared and organized"
    },
    "ESFJ": {
        "Clothing": "Preppy and polished attire",
        "Colors": "Soft and feminine colors such as pastels and blush tones",
        "Fit": "Tailored and figure-flattering",
        "Textures and Fabrics": "Soft and comfortable fabrics",
        "Accessories": "Feminine and elegant accessories",
        "Hair and Makeup": "Neat and styled hair, natural makeup with a touch of blush",
        "Footwear": "Classic heels or stylish flats",
        "Layering": "Layer with cardigans or scarves for a feminine touch",
        "Personal Touches": "Add delicate jewelry or a floral accessory",
        "Confidence": "Confidence comes from connecting with others and being supportive"
    },
    "ISTP": {
        "Clothing": "Functional and practical attire",
        "Colors": "Neutral and earthy tones",
        "Fit": "Fitted but comfortable",
        "Textures and Fabrics": "Durable and rugged fabrics",
        "Accessories": "Utilitarian accessories",
        "Hair and Makeup": "Low-maintenance hairstyle, minimal makeup",
        "Footwear": "Sturdy and supportive shoes",
        "Layering": "Layer with lightweight and versatile pieces",
        "Personal Touches": "Add a rugged watch or outdoor-inspired accessories",
        "Confidence": "Confidence comes from being prepared for any situation"
    },
    "ISFP": {
        "Clothing": "Bohemian and artistic attire",
        "Colors": "Soft and muted colors, pastel shades",
        "Fit": "Flowy and relaxed",
        "Textures and Fabrics": "Natural and organic fabrics",
        "Accessories": "Handmade or artisanal accessories",
        "Hair and Makeup": "Messy or bohemian hairstyle, minimal makeup",
        "Footwear": "Comfortable and stylish sandals or boots",
        "Layering": "Layer with lightweight scarves or shawls",
        "Personal Touches": "Express your creativity through handmade or unique items",
        "Confidence": "Confidence comes from embracing your individuality and creativity"
    },
     "ESTP": {
        "Clothing": "Edgy and bold attire",
        "Colors": "Vibrant and daring colors such as red, orange, and electric blue",
        "Fit": "Fitted and attention-grabbing",
        "Textures and Fabrics": "Leather, denim, and other rugged materials",
        "Accessories": "Statement accessories such as chunky jewelry or bold belts",
        "Hair and Makeup": "Trendy hairstyles with bold colors or highlights, bold makeup looks",
        "Footwear": "Stylish sneakers or boots with attitude",
        "Layering": "Layer with graphic tees, hoodies, or bomber jackets",
        "Personal Touches": "Express your individuality with unique tattoos or piercings",
        "Confidence": "Confidence comes from embracing your unique style and spontaneity"
    },
    "ESFP": {
        "Clothing": "Fun and eclectic attire",
        "Colors": "Bright and cheerful colors such as yellow, pink, and turquoise",
        "Fit": "Flattering and comfortable",
        "Textures and Fabrics": "Soft and playful fabrics like cotton or chiffon",
        "Accessories": "Whimsical accessories like statement earrings or colorful scarves",
        "Hair and Makeup": "Playful hairstyles with braids or curls, vibrant makeup looks",
        "Footwear": "Fashionable sandals or flats with unique details",
        "Layering": "Layer with flowy tops, cardigans, or patterned skirts",
        "Personal Touches": "Show your outgoing personality with expressive gestures and laughter",
        "Confidence": "Confidence comes from being outgoing and embracing your vibrant personality"
    }
}


    body_type_recommendations = {
    "Ectomorph": {
        "Fit": "Structured pieces to add volume",
        "Footwear": "Avoid chunky styles, opt for sleek designs",
        "Layering": "Layer with light fabrics and structured outerwear",
        "Colors": "Neutral colors such as beige, gray, and white",
        "Textures and Fabrics": "Textured fabrics like tweed or knit for added dimension",
        "Accessories": "Delicate accessories like dainty necklaces or bracelets"
    },
    "Endomorph": {
        "Fit": "Tailored pieces to streamline the silhouette",
        "Footwear": "Sturdy shoes with good arch support",
        "Layering": "Layer with lightweight fabrics to avoid bulkiness",
        "Colors": "Dark colors to create a slimming effect",
        "Textures and Fabrics": "Smooth and stretchy fabrics for comfort",
        "Accessories": "Subtle accessories like small earrings or thin belts"
    },
    "Mesomorph": {
        "Fit": "Fitted styles to highlight the athletic physique",
        "Footwear": "Stylish and supportive athletic shoes or boots",
        "Layering": "Layer with fitted pieces to showcase muscle definition",
        "Colors": "Bold colors such as red, blue, and green",
        "Textures and Fabrics": "Durable and breathable fabrics like denim or cotton",
        "Accessories": "Bold accessories to complement the strong features, like statement watches or sunglasses"
    }
}

    body_language_recommendations = {
        "Lookers": {
            "Colors": "Bold and eye-catching colors",
            "Textures and Fabrics": "Textured fabrics for visual interest",
            "Accessories": "Statement accessories to draw attention"
            # Add more recommendations as needed
        },
        "Listeners": {
            "Colors": "Soft and muted colors for a calming effect",
            "Textures and Fabrics": "Soft and comfortable fabrics",
            "Accessories": "Subtle accessories that don't distract"
            # Add more recommendations as needed
        },
        "Touchers": {
            "Textures and Fabrics": "Rich and tactile fabrics",
            "Accessories": "Accessories with interesting textures"
            # Add more recommendations as needed
        }
    }

    personalized_recommendations = {}
    personalized_recommendations.update(recommendations.get(mbti_type, {}))
    personalized_recommendations.update(body_type_recommendations.get(body_type, {}))
    personalized_recommendations.update(body_language_recommendations.get(body_language, {}))

    return personalized_recommendations


def main():
    print("***** Personality Classification *****")
    mbti_type = classify_mbti()
    body_type = classify_body_type()
    body_language = classify_body_language()
    print("***** Wardrobe Suggestions *****")
    print(mbti_type,body_type,body_language)
    recommendations = personalized_clothing_recommendations(mbti_type, body_type, body_language)
    for category, recommendation in recommendations.items():
        print(f"{category}: {recommendation}")

if __name__ == "__main__":
    main()
