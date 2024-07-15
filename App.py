import streamlit as st
import random
from streamlit_elements import elements, mui, html, sync

# Définition des options pour chaque roulette
race_options = ["Humain", "Homme-Poisson", "Géant", "Mink", "Longarm", "Longleg", "Skypien", "Tontatta"]
birthplace_options = ["East Blue", "West Blue", "South Blue", "North Blue", "Grand Line", "New World", "Île des Hommes-Poissons", "Skypiea", "Île des Géants (Elbaf)", "Zou"]
haki_options = ["Pas de Haki", "Haki de l'Observation - Niveau 1", "Haki de l'Observation - Niveau 2", "Haki de l'Observation - Niveau 3", "Haki de l'Armement - Niveau 1", "Haki de l'Armement - Niveau 2", "Haki de l'Armement - Niveau 3", "Haki des Rois - Niveau 1", "Haki des Rois - Niveau 2", "Haki des Rois - Niveau 3"]
fruit_options = ["Pas de Fruit du Démon", "Paramecia - Niveau de Maîtrise 1", "Paramecia - Niveau de Maîtrise 2", "Paramecia - Niveau de Maîtrise 3", "Zoan - Niveau de Maîtrise 1", "Zoan - Niveau de Maîtrise 2", "Zoan - Niveau de Maîtrise 3", "Logia - Niveau de Maîtrise 1", "Logia - Niveau de Maîtrise 2", "Logia - Niveau de Maîtrise 3"]
combat_style_options = ["Combat à mains nues", "Épéiste", "Tireur d'élite", "Art martial des Hommes-Poissons", "Rokushiki", "Utilisateur d'armes (marteau, lance, etc.)", "Ninpo"]
combat_mastery_options = ["Niveau Débutant", "Niveau Intermédiaire", "Niveau Avancé", "Maître"]
intelligence_options = ["Très faible", "Faible", "Moyenne", "Élevée", "Très élevée"]
speed_options = ["Très lente", "Lente", "Moyenne", "Rapide", "Très rapide"]
resistance_options = ["Très faible", "Faible", "Moyenne", "Élevée", "Très élevée"]
affiliation_options = ["Pirate", "Marine", "Révolutionnaire", "Chasseur de Primes", "Civil"]
adventure_options = ["Affronte la Marine", "Rejoint un équipage de pirates connu (Luffy, Kid, Law, etc.)", "Trouve un Fruit du Démon (vendre, manger, donner)", "Affronte un autre pirate célèbre", "Découvre une île mystérieuse", "Capture par la Marine", "Rencontre un ancien personnage de la série (Rayleigh, Shanks, etc.)", "Participe à une guerre majeure (Marineford, etc.)", "Reçoit un objet spécial d'un marchand"]
training_options = ["Augmente l'Intelligence", "Augmente la Vitesse", "Augmente la Résistance", "Améliore la maîtrise du Haki", "Améliore la maîtrise du Fruit du Démon", "Améliore la maîtrise du style de combat", "Trouve un mentor pour un entraînement intensif"]
major_event_options = ["Marineford", "Dressrosa", "Wano", "Reverie", "Impel Down", "Punk Hazard", "Whole Cake Island"]
merchant_options = ["Achète une arme spéciale", "Achète une armure résistante", "Achète des médicaments pour booster la résistance", "Achète un Log Pose pour une île spéciale", "Achète des informations cruciales"]
immortality_options = ["Obtient le statut d'immortel", "Ne devient pas immortel"]

# Fonction pour tourner une roulette
def spin_wheel(options):
    return random.choice(options)

# Génération du personnage
def generate_character():
    character = {
        "Race": spin_wheel(race_options),
        "Lieu de Naissance": spin_wheel(birthplace_options),
        "Haki": spin_wheel(haki_options),
        "Fruit du Démon": spin_wheel(fruit_options),
        "Style de Combat": spin_wheel(combat_style_options),
        "Maîtrise du Style de Combat": spin_wheel(combat_mastery_options),
        "Intelligence": spin_wheel(intelligence_options),
        "Vitesse": spin_wheel(speed_options),
        "Résistance": spin_wheel(resistance_options),
        "Affiliation": spin_wheel(affiliation_options)
    }
    return character

# Génération de l'histoire
def generate_story(character):
    story = {
        "Péripétie": spin_wheel(adventure_options),
        "Entraînement": spin_wheel(training_options),
        "Événement Majeur": spin_wheel(major_event_options),
        "Marchand": spin_wheel(merchant_options),
        "Immortalité": spin_wheel(immortality_options)
    }
    return story

# Affichage du personnage et de son histoire
def display_character(character):
    st.write("### Personnage")
    for key, value in character.items():
        st.write(f"**{key}**: {value}")

def display_story(story):
    st.write("\n### Histoire")
    for key, value in story.items():
        st.write(f"**{key}**: {value}")

# Initialisation du personnage et de l'histoire
if "character" not in st.session_state:
    st.session_state.character = generate_character()
if "story" not in st.session_state:
    st.session_state.story = generate_story(st.session_state.character)

# Streamlit UI
st.title("One Piece Roulette Game")
st.write("Créez votre propre personnage et son histoire dans l'univers de One Piece en tournant les roulettes!")

with st.sidebar:
    if st.button('Générer Race'):
        st.session_state.character["Race"] = spin_wheel(race_options)
    if st.button('Générer Lieu de Naissance'):
        st.session_state.character["Lieu de Naissance"] = spin_wheel(birthplace_options)
    if st.button('Générer Haki'):
        st.session_state.character["Haki"] = spin_wheel(haki_options)
    if st.button('Générer Fruit du Démon'):
        st.session_state.character["Fruit du Démon"] = spin_wheel(fruit_options)
    if st.button('Générer Style de Combat'):
        st.session_state.character["Style de Combat"] = spin_wheel(combat_style_options)
    if st.button('Générer Maîtrise du Style de Combat'):
        st.session_state.character["Maîtrise du Style de Combat"] = spin_wheel(combat_mastery_options)
    if st.button('Générer Intelligence'):
        st.session_state.character["Intelligence"] = spin_wheel(intelligence_options)
    if st.button('Générer Vitesse'):
        st.session_state.character["Vitesse"] = spin_wheel(speed_options)
    if st.button('Générer Résistance'):
        st.session_state.character["Résistance"] = spin_wheel(resistance_options)
    if st.button('Générer Affiliation'):
        st.session_state.character["Affiliation"] = spin_wheel(affiliation_options)

# Affichage du personnage et de son histoire
display_character(st.session_state.character)
display_story(st.session_state.story)

# Animation du personnage
with elements("animation"):
    html.div(id="character-animation", style={"width": "100%", "height": "300px", "backgroundColor": "#f0f0f0", "display": "flex", "alignItems": "center", "justifyContent": "center"})

    # Synchronisation des états
    with sync():
        # Mise à jour du contenu de l'animation
        html.div(f"Roue tournante: {random.choice(['Race', 'Lieu de Naissance', 'Haki', 'Fruit du Démon', 'Style de Combat', 'Maîtrise du Style de Combat', 'Intelligence', 'Vitesse', 'Résistance', 'Affiliation'])}",
                 key="animation-content")
