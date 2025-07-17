from src.examples.utils import mix_topic_samples

pizza = """To make a Neapolitan pizza, you must first activate the yeast in warm water.
The dough should be kneaded until it passes the windowpane test.
Let the dough cold ferment for 24-72 hours to develop complex flavors.
The pizza stone must be preheated for at least 30 minutes at maximum temperature.
Fresh basil should only be added to the pizza after it comes out of the oven.
A light drizzle of extra virgin olive oil completes the authentic Margherita.
Proper pizza dough hydration should be between 65% and 70%.
The perfect pizza requires a careful balance of sauce and cheese ratios.
San Marzano tomatoes are the traditional choice for pizza sauce.
Their sweet-tart flavor and low water content make them ideal for pizzas.
The pizza must be rotated halfway through cooking for even browning."""

bike = """A proper bike chain maintenance routine includes regular degreasing and lubrication.
Replacing bike brake pads requires careful alignment with the rim surface.
Always test the brakes before riding after any maintenance work.
Tubeless bike tires require special sealant to prevent punctures.
A bike's bottom bracket needs regular greasing to prevent creaking.
Chainring wear can be measured with a simple gauge tool.
Bike disc brake rotors should be cleaned with isopropyl alcohol.
Regular maintenance extends the life of your braking system."""

economics = """The Federal Reserve announced a 25 basis point increase in interest rates.
The yield curve inversion suggested an impending recession.
Market volatility increased as geopolitical tensions escalated.
The GDP growth forecast was revised down by 0.5 percentage points.
The Bank of England maintained its quantitative easing program.
Brexit negotiations stalled over Northern Ireland protocol disputes.
The supply chain disruption led to increased inflationary pressures.
Global shipping costs tripled due to port congestion.
Fiscal policy became more expansionary as unemployment rose.
Government spending increased to stimulate economic growth.
Inflation targeting became the dominant monetary policy framework.
The marginal cost curve intersects with average total cost at its minimum point."""

football = """Manchester United's striker missed a crucial penalty in stoppage time.
Arsenal's defensive line pushed high up the pitch, risking counter-attacks.
The opposition exploited the space behind with quick transitions.
Liverpool's high-pressing system overwhelmed the opposition midfield.
Chelsea's new American owner invested heavily in young talent.
Their transfer strategy focused on players under twenty-three.
The academy graduates were integrated into the first team.
Tottenham's counter-attacking style relied heavily on Son's pace.
Newcastle United's Saudi ownership transformed their transfer policy."""

lotr = """Frodo carried the One Ring through the perilous lands of Mordor.
Gandalf the Grey fell in battle with the Balrog of Morgoth.
The fellowship watched in horror as he plunged into the abyss of Khazad-dûm.
Sauron's armies gathered at the Black Gate for the final battle.
Aragorn claimed his throne as the King of Gondor and Arnor.
The Hobbits' journey began in the peaceful Shire with second breakfast.
Samwise Gamgee was the true hero of the Lord of the Rings.
His unwavering loyalty and courage carried Frodo to Mount Doom.
Gollum's tragic story began with his discovery of the precious ring.
The ring's corruption slowly destroyed his mind over five hundred years.
The Riders of Rohan arrived at dawn on the fifth day.
Their horns echoed across Helm's Deep as hope returned to the defenders.
The Eagles could have flown the ring to Mordor, but that's not the point."""

anime = """Naruto mastered the Rasengan technique after weeks of training.
Sasuke's Sharingan evolved into the Mangekyo after experiencing great loss.
Goku achieved Ultra Instinct in his battle against Jiren.
Attack on Titan's final season revealed the truth about the Founding Titan.
Eren's motivations became clear as the dark history unfolded.
One Piece's Gear Fifth transformation defied all known Devil Fruit rules.
Luffy's awakening brought both power and unprecedented freedom to his abilities.
Demon Slayer's breathing techniques were inspired by ancient martial arts.
Death Note explored complex themes of justice and morality.
My Hero Academia's quirk system revolutionized the superhero genre."""

# Create topics dictionary with raw text strings
topics = {
    "pizza": pizza,
    "bike": bike,
    "economics": economics,
    "football": football,
    "lotr": lotr,
    "anime": anime,
}

# Create mixed sample using utility function
mixed_topics_chaos = mix_topic_samples(topics, min_lines=2, max_lines=3)

# create a joined string of the topics
mixed_topics = "\n".join(topics.values())
