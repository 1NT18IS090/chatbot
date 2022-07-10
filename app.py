from flask import Flask, render_template, request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)



# Creating ChatBot Instancep

bot = ChatBot("My Bot")
convo = [
    'hey',
    'hi, i am eva . i am here to guide you through the covid 19 self checker',
    'hey how are you ?',
    'i am good ',
    'where do you live ?',
    'i live in banglore',
    'how was your day ?',
    'it was great day , i made lot of progress',
    'can you suggest a series ?',
    ' you can watch how i met your mother if you like comdey series',
    'What is COVID-19 ?',
    'COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2.  WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.',
    'What is the symptoms of covid 19 ?',
    'The most common sysmptoms of covid 19 are fever, dry cough and fatigue',
    'What happens to people who get covid 19 ?',
    'Among those who develop symptoms, most (about 80%) recover from the disease without needing hospital treatment. About 15% become seriously ill and require oxygen and 5% become critically ill and need intensive care.',
    'Who is most at risk of severe illness from covid 19 ?',
    'People aged 60 years and over, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, obesity or cancer, are at higher risk of developing serious illness. ',
    'Are there longterm effects of covid 19 ?',
    'Some people who have had COVID-19, whether they have needed hospitalization or not, continue to experience symptoms, including fatigue, respiratory and neurological symptoms',
    'How can we protect others and ourselves if we dont know who is infected ?',
    'Stay safe by taking some simple precautions, such as physical distancing, wearing a mask, especially when distancing cannot be maintained, keeping rooms well ventilated, avoiding crowds and close contact, regularly cleaning your hands, and coughing into a bent elbow or tissue. Check local advice where you live and work. Do it all!',
    'When should i get a test for covid 19 ?',
    'Anyone with symptoms should be tested, wherever possible. People who do not have symptoms but have had close contact with someone who is, or may be, infected may also consider testing – contact your local health guidelines and follow their guidance.',
    'What test should i get to see if i have covid 19 ?',
    'In most situations, a molecular test is used to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction (PCR) is the most commonly used molecular test. Samples are collected from the nose and/or throat with a swab',
    'Who made you ?',
    'i was made by panel 12 ',
    'What about rapid tests ?',
    'Rapid antigen tests (sometimes known as a rapid diagnostic test – RDT) detect viral proteins (known as antigens). Samples are collected from the nose and/or throat with a swab. ',
    'I want to find out if i had covid 19 in past , what test could i take ?',
    'Antibody tests can tell us whether someone has had an infection in the past, even if they have not had symptoms. Also known as serological tests and usually done on a blood sample, these tests detect antibodies produced in response to an infection',
    'What is the difference between isolation and quarantine ?',
    'Both isolation and quarantine are methods of preventing the spread of COVID-19. Quarantine is used for anyone who is a contact of someone infected with the SARS-CoV-2 virus, which causes COVID-19, whether the infected person has symptoms or not. Isolation is used for people with COVID-19 symptoms or who have tested positive for the virus. Being in isolation means being separated from other people, ideally in a medically facility where you can receive clinical care.  ',
    'What should i do if i have been exposed to someone who has covid 19 ?',
    'After exposure to someone who has COVID-19 Call your health care provider or COVID-19 hotline to find out where and when to get a test.',
    'How long does it take to develop symptoms ?',
    'The time from exposure to COVID-19 to the moment when symptoms begin is, on average, 5-6 days and can range from 1-14 days. This is why people who have been exposed to the virus are advised to remain at home and stay away from others, for 14 days, in order to prevent the spread of the virus, especially where testing is not easily available',
    'Is there a vaccine for covid 19 ?',
    'es. The first mass vaccination programme started in early December 2020 and the number of vaccination doses administered is updated on a daily basis here. At least 13 different vaccines (across 4 platforms) have been administered. Campaigns have started in 206 economies',
    'What should i do if i have covid 19 symptoms ?',
    'Are there treatments for covid 19 ?',
    'Scientists around the world are working to find and develop treatments for COVID-19.',
    'Are antibiotics effective in preventing or treating covid 19 ?',
    'Antibiotics do not work against viruses; they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19.',
    'How to take care of COVID-19? ',
    'Daily, eat: 2 cups of fruit (4 servings), 2.5 cups of vegetables (5 servings), 180 g of grains, and 160 g of meat and beans (red meat can be eaten 1−2 times per week, and poultry 2−3 times per week). For snacks, choose raw vegetables and fresh fruit rather than foods that are high in sugar, fat or salt.',
    'What is the FDA doing to respond to the COVID-19 pandemic?',
    ' The FDA, along with other federal, state, and local agencies and public health officials across the country and internationally, plays a critical role in protecting public health during the COVID-19 pandemic. FDA staff are working around the clock to support development of  medical countermeasures and are providing regulatory advice, guidance, and technical assistance to advance the development and availability of vaccines, therapies, diagnostic tests and other medical devices for use diagnosing, treating, and preventing this novel virus. The FDA continues to monitor the human and animal food supply and take swift action on fraudulent COVID-19 products.',
    ' What is an emergency use authorization and how is it being used to respond to COVID-19?',
    'An emergency use authorization (EUA) is a mechanism to facilitate the availability and use of medical countermeasures, including vaccines, tests, and medicines, during public health emergencies, such as the current COVID-19 pandemic. Under an EUA, the FDA may allow the use of unapproved medical products, or unapproved uses of approved medical products in an emergency to diagnose, treat, or prevent serious or life-threatening diseases or conditions when certain statutory criteria have been met, including that there are no adequate, approved, and available alternatives. Taking into consideration input from the FDA, manufacturers decide whether and when to submit an EUA request to the FDA',
    'How can I prevent COVID-19?',
    'The best way to prevent COVID-19 is to get vaccinated with an FDA-approved or FDA-authorized COVID-19 vaccine and stay up to date on your COVID-19 vaccines.',
    'What treatments are available in the U.S. to treat COVID-19?',
    'The FDA has approved and authorized treatments for COVID-19 for emergency use during this public health emergency. View the FDA’s Emergency Use Authorization (EUA) page to see all products authorized to treat COVID-19. Read our article: Know Your Treatment Options for COVID-19.',
    ' Will Miracle Mineral Solution (MMS) cure COVID-19?',
    ' No. Miracle Mineral Solution does not cure COVID-19 and has not been approved by the FDA for any use. The solution, when mixed as directed, forms industrial bleach that may cause serious and potentially life-threatening side effects. The FDA took action against Genesis II Church of Health and Healing for unlawfully distributing Miracle Mineral Solution for the treatment of COVID-19 and other diseases. Learn more: Danger: Don’t Drink Miracle Mineral Solution or Similar Products. ',
    ' Is hand sanitizer effective against COVID-19?',
    ' One of the best ways to prevent the spread of infections and decrease the risk of getting sick is by washing your hands with plain soap and water, advises the CDC. Washing hands often with soap and water for at least 20 seconds is essential, especially after going to the bathroom; before eating; and after coughing, sneezing, or blowing one’s nose. If soap and water are not available, CDC recommends consumers use an alcohol-based hand sanitizer that contains at least 60% alcohol.',
    ' What do I do if I get a rash or other reaction to hand sanitizer? What do I do if I have been exposed to contaminated hand sanitizer?',
    'Call your doctor if you experience a serious reaction to hand sanitizer. People who have been exposed to contaminated hand sanitizer and are experiencing symptoms should seek immediate medical treatment for potential reversal of toxic effects.',
    'What is the risk of using a hand sanitizer that contains methanol (wood alcohol) or 1-propanol?',
    ' Methanol exposure can result in nausea, vomiting, headache, blurred vision, permanent blindness, seizures, coma, permanent damage to the nervous system or death. Although people using these products on their hands are at risk for methanol poisoning, young children who accidentally swallow these products and adolescents and adults who drink these products as an alcohol (ethanol) substitute are most at risk.',
    ' What should I do with hand sanitizer on the FDAs list of hand sanitizers that consumers should not use?',
    'If you have one of the products on the FDAs list of hand sanitizers consumers should not use, immediately stop using it and dispose of the product ideally in a hazardous waste container. Do not pour these products down the drain or flush them. Contact your local waste management and recycling center for more information on hazardous waste disposal. Learn how to search the FDAs hand sanitizer list, including a description of how to search for manufacturers and distributors on the label',
    ' Does spraying people with disinfectant, or having people go through disinfectant tunnels, walkways, or chambers, lower the spread of COVID-19?',
    'No. The FDA does not recommend spraying humans with aerosolized disinfectant. At this time, there is a lack of data to demonstrate that sanitation tunnels are effective in reducing the spread of or in treating COVID-19.',

    ' Products online claim to prevent or treat COVID-19. Where can I report websites selling products with fraudulent claims?',
    'The FDA advises consumers to be beware of websites and stores selling products that claim to prevent, treat, or cure COVID-19. If you have a question about a product sold online that claims to prevent, treat, or cure COVID-19, talk to your health care provider or doctor.',
    ' Am I at risk for serious complications from COVID-19 if I smoke cigarettes?',
    'Yes. Data shows that when compared to never smokers, cigarette smoking increases the risk of more severe illness from COVID-19, which could result in hospitalization, the need for intensive care, or even death. Smoking cigarettes can cause inflammation and cell damage throughout the body, and can weaken your immune system, making it less able to fight off disease',
    ' If I vape tobacco or nicotine am I at risk for complications from COVID-19?',
    'E-cigarette use can expose the lungs to toxic chemicals, but whether those exposures increase the risk of COVID-19 or the severity of COVID-19 outcomes is not known. However, many e-cigarette users are current or former smokers, and cigarette smoking increases the risk of respiratory infections, including pneumonia.',
    'What is the FDA process for a COVID-19 vaccine authorized for emergency use versus an FDA-approved COVID-19 vaccine?',
    'Emergency use authorizations (EUAs) can be used by the FDA during public health emergencies to provide access to unapproved vaccines (or unapproved uses of an approved vaccine) that may be effective in preventing a disease. Emergency use authorization is a tool that the FDA can use in a declared public health emergency, like the current pandemic, to more rapidly make available potentially life-saving products under very specific conditions. In determining whether to issue an EUA for a vaccine, after the FDA receives a request for an EUA, the agency evaluates the data submitted, conducts its own analyses and assesses any known or potential risks and any known or potential benefits.',
    'Which COVID-19 vaccines are FDA-approved or authorized for emergency use?',
    'Comirnaty (COVID-19 Vaccine, mRNA)',
    ' Am I eligible for a first booster dose of a COVID-19 vaccine, and if so, which one?',
    ' Ages 5 through 11 years: may receive a single booster dose at least five months after completion of a primary vaccine series with the Pfizer-BioNTech COVID-19 Vaccine.  This age group may receive only the Pfizer-BioNTech COVID-19 Vaccine as their booster dose.',
    'Am I eligible for a second COVID-19 vaccine booster dose?',
    ' If it has been at least 4 months since your first booster dose of any authorized or approved COVID-19 vaccine and you are an individual 50 years of age or older or an individual 12 years of age or older with certain kinds of immunocompromise, you may receive a second COVID-19 vaccine booster dose.',
    ' Which COVID-19 vaccines have the FDA authorized for administration of an additional primary series dose for immunocompromised individuals?',
    'For individuals who have undergone solid organ transplantation, or who are diagnosed with conditions that are considered to have an equivalent level of immunocompromise, the following COVID-19 vaccines are authorized for administration of an additional primary series dose',
    ' How does the FDA ensure the quality of COVID-19 vaccines and other medical products authorized for emergency use in the U.S.?',
    'The FDA takes very seriously its responsibility to ensure the quality of vaccines and other medical products for use during this pandemic. The agency is using a variety of inspectional tools to help ensure that products being produced in different facilities meet the high-quality standards that the public has come to expect. The FDA will continue to work with companies to ensure that the quality standards that it expects for products distributed under an emergency use authorization are met, and will continue to work diligently to help bring needed medical products in a timely manner to Americans during this public health emergency.',
    ' How do I report COVID-19 vaccine side effects?',
    ' If you experience a severe allergic reaction or any life-threatening symptoms such as trouble breathing, call 911, or go to the nearest hospital.',
    ' Can a COVID-19 vaccine cause infertility in women?',
    ' There is no scientific evidence to suggest that FDA-authorized or FDA-approved COVID-19 vaccines could cause infertility in women. In addition, infertility is not known to occur as a result of natural COVID-19 disease, further demonstrating that immune responses to the virus, whether induced by infection or a vaccine, are not a cause of infertility. Reports on social media have falsely asserted that the COVID-19 vaccine could cause infertility in women and the FDA is concerned that this misinformation may cause women to avoid vaccination to prevent COVID-19, which is a potentially serious and life-threatening disease. The symptoms of COVID-19 vary and are unpredictable; many people have no symptoms or only mild disease, while some have severe respiratory disease including pneumonia and acute respiratory distress syndrome (ARDS), leading to multi-organ failure and death.',
    ' Can the FDA help me get a COVID-19 vaccine?',
    'No. The FDA’s authority includes authorizing or approving COVID-19 vaccines for use in the U.S., but the FDA is not responsible for vaccine distribution. Search vaccines.gov, text your zip code to 438829, or call 1-800-232-0233 to find COVID-19 vaccine locations near you',
    ' Do any of the COVID-19 vaccines authorized for emergency use or approved by the FDA contain a live form of the SARS-CoV-2 virus (the virus that causes COVID-19 disease)?',
    'None of the currently FDA-authorized or approved vaccines contain the live SARS-CoV-2 virus, and you can’t get COVID-19 from the vaccines.',
    ' Are egg products used in COVID-19 vaccines?',
    ' No. The COVID-19 vaccines currently authorized or approved by the FDA are not manufactured using egg products or egg culture. See COVID-19 vaccines for more information.',
    ' Can SARS-CoV-2, the virus that causes COVID-19, be transmitted by blood transfusion?',
    'In general, respiratory viruses are not known to be transmitted by blood transfusion, and there have been no reported cases of transfusion-transmitted coronavirus worldwide.',
    'What steps are being taken to protect the U.S. blood supply from SARS-CoV-2, the virus that causes COVID-19?',
    'Blood donors must be healthy and feel well on the day of donation. Routine blood donor screening measures that are already in place should prevent individuals with clinical respiratory infections from donating blood. For example, blood donors must be in good health and have a normal temperature on the day of donation.',
    ' Why aren’t blood centers testing donors for SARS-CoV-2?',
    'The FDA does not recommend using laboratory tests to screen blood. Someone who has symptoms of COVID-19, including fever, cough, and shortness of breath, is not healthy enough to donate blood. Standard screening processes already in place will mean that someone with these symptoms will not be allowed to donate. ',
    ' Is it safe for me to donate blood during the COVID-19 pandemic?',
    'It is imperative that eligible individuals continue to donate blood and blood components, including source plasma, during the pandemic. If you are healthy and interested in donating blood, the FDA encourages you to contact a local donation center to make an appointment. One way to make a difference during a public health emergency is to donate blood if you are able',
    ' Can I donate blood following receipt of a COVID-19 vaccine?',
    'Yes, individuals who receive a nonreplicating, inactivated or mRNA-based COVID-19 vaccine can donate blood without a waiting period.',
    ' What is convalescent plasma and why is it being investigated to treat COVID-19?',
    'Convalescent refers to anyone recovering from a disease. Plasma is the yellow, liquid part of blood that contains antibodies. Antibodies are proteins made by the body in response to infections.  Convalescent plasma from patients who have already recovered from coronavirus disease 2019 (COVID-19)',
    ' What does it mean to be an FDA-approved drug?',
    'FDA approval of a drug means that the agency has determined, based on substantial evidence, that the drug is effective for its intended use, and that the benefits of the drug outweigh its risks when used according to the product’s approved labeling. The drug approval process takes place within a structured framework that includes collecting clinical data and submitting an application to the FDA',
    ' What is the FDA’s role in regulating potential treatments during a public health emergency?',
    'The FDA carries out many activities to protect and promote public health during a public health emergency, including helping to accelerate the development and availability of potential treatments, protecting the security of drug supply chains, providing guidance to food and medical device manufacturers, advising developers on clinical trial issues, and keeping the public informed with authoritative health information.',
    ' What drugs (medicines) are available in the U.S. to treat COVID-19?',
    'The FDA has approved and authorized treatments for COVID-19 for emergency use during this public health emergency. View the FDA’s Emergency Use Authorization (EUA) page to see all products authorized to treat COVID-19. Products that have been approved to treat COVID-19 without any remaining EUA authorized uses can be found on the FDA’s COVID-19 Drugs page. Read our article: Know Your Treatment Options for COVID-19.',
    ' What is a monoclonal antibody?',
    'Monoclonal antibodies are laboratory-produced molecules that act as substitute antibodies that can restore',
    ' Where are infusions of monoclonal antibody treatments available?',
    'Monoclonal antibody treatments for COVID-19 may only be administered in settings in which health care providers have immediate access to medications to treat a severe infusion reaction, such as anaphylaxis, and have the ability to activate the emergency medical system (EMS), if necessary. Please speak with your doctor or contact your local or state public health department for more information.',
    ' Are chloroquine phosphate or hydroxychloroquine sulfate approved by the FDA to treat COVID-19?',
    'No. Hydroxychloroquine sulfate and some versions of chloroquine phosphate are FDA-approved to treat malaria. Hydroxychloroquine sulfate is also FDA-approved to treat lupus and rheumatoid arthritis',
    ' Should I take chloroquine phosphate used to treat disease in aquarium fish to prevent or treat COVID-19?',
    ' No. Products marketed for veterinary use, “for research only,” or otherwise not for human consumption have not been evaluated for safety or effectiveness and should never be used by humans',
    ' Are antibiotics effective in preventing or treating COVID-19?',
    ' No. Antibiotics do not work against viruses; they only work on bacterial infections. Antibiotics do not prevent or treat COVID-19, ',
    ' Should I take ivermectin to prevent or treat COVID-19?',
    'We have established a cross-agency team dedicated to closely monitoring for fraudulent COVID-19 products. In response to internet scammers, the FDA has taken – and continues to take – actions regarding unapproved products that are distributed with fraudulent claims to prevent, treat, diagnose or cure COVID-19.',
    'Are there drug shortages due to COVID-19?',
    'The FDA has been closely monitoring the supply chain with the expectation that the COVID-19 outbreak would likely impact the medical product supply chain, including potential disruptions to supply or shortages of critical medical products in the U.S. ',
    ' Who should I contact with drug-related questions?',
    'f you have additional questions, call the FDA’s Division of Drug Information at (855) 543-3784 or email us at druginfo@fda.hhs.gov. ',
    'What types of COVID-19 tests are available?',
    'There are different types of COVID-19 tests. Diagnostic tests can show if you have an active COVID-19 infection. Antibody or serology tests look for antibodies in a blood sample to determine if an individual has had a past infection with the virus that causes COVID-19 but cannot be used to diagnose current COVID-19 infection.',
    'What at-home over-the-counter (OTC) tests for COVID-19 are authorized by the FDA?',
    'Search the list of FDA-authorized at-home over-the-counter (OTC) COVID-19 diagnostic tests',

    'Do COVID-19 tests check for delta, omicron, or other variants?',
    'The SARS-CoV-2 virus, which causes COVID-19, has mutated over time, resulting in genetic variants over the course of the COVID-19 pandemic. COVID-19 diagnostic tests are designed to detect all known variants. However, they are typically not able to identify the specific type of SARS-CoV-2 variant ',

    'Is there a shortage of personal protective equipment (PPE) such as medical gloves and surgical N95 respirators?',
    'Yes, please refer to the FDA’s current device shortage list. This list reflects the categories of devices the FDA has determined to be in shortage at this time and will be maintained and updated as the COVID-19 public health emergency evolves. The presence of a device type on this list does not necessarily indicate that patient care has been or will be affected.',

    'Can 3D printing be used to make PPE?',
    'Find FDAs guidance about 3D printing during the COVID-19 pandemic.',
    'How is the FDA helping ensure that ventilators are available for patients who need them?',
    'The FDA continues to work with manufacturers and sponsors of ventilators and other respiratory support devices and accessories to help make these devices available through the emergency use authorization (EUA) process.',

    'Who should I contact if I have questions about medical devices or need more information?',

    'Please see Contacts for Medical Devices During the COVID-19 Pandemic.',
    'What is the FDA’s role in helping to ensure the safety of the human and animal food supply?',
    'To protect public health, the FDA monitors domestic firms and the foods that they produce. The FDA also monitors imported products and foreign firms exporting to the U.S. The FDA protects consumers from unsafe foods through research and methods development; inspection and sampling; and regulatory and legal action.',

    'Why is the FDA providing flexibility to food manufacturers, under limited circumstances during the COVID-19 public health emergency, to make minor changes in ingredients without reflecting those changes on the package label?',
    ' Due to limited shortages of specific ingredients and foods, or unexpected supply chain disruptions in some industries, food manufacturers may need to make small changes to some ingredients during the COVID-19 public health emergency. Manufacturers may not be able to relabel their products to reflect these minor changes on the food label without slowing down the processing or distribution of the food.',

    'What do I need to know about the temporary policy for food labeling of minor ingredient changes during the COVID-19 public health emergency if I have food allergies?',
    'Although the temporary policy allows some flexibility, the eight major food allergens under the Food Allergen Labeling and Consumer Protection Act (FALCPA) of 2004 cannot be substituted for labeled ingredients by manufacturers without a corresponding label change.',

    'What are the most important things I need to know to keep myself and others safe when I go to the grocery store during the pandemic?',
    'There are steps you can take to help protect yourself, grocery store workers and other shoppers, such as wearing a face covering, practicing social distancing, and using wipes on the handles of the shopping cart or basket.',

    'Are food products produced in the U.S. or other countries affected by COVID-19 a risk for the spread of COVID-19?',
    'There is no evidence to suggest that food produced in the United States or imported from countries affected by COVID-19 can transmit COVID-19.',

    'Can I get the coronavirus from food, food packaging, or food containers and preparation area?',
    'Currently there is no evidence of food, food containers, or food packaging being associated with transmission of COVID-19.  Like other viruses, it is possible that the virus that causes COVID-19 can survive on surfaces or objects. ',

    'Is the U.S. food supply safe?',
    'Currently there is no evidence of food or food packaging being associated with transmission of COVID-19.  ',
    'Can I get COVID-19 from a food worker handling my food?',
    'Currently, there is no evidence of food or food packaging being associated with transmission of COVID-19. However, the virus that causes COVID-19 spreads from person-to-person. The CDC recommends that if you are sick, stay home until you are better and no longer pose a risk of infecting others. ',

    'Should food facilities (grocery stores, manufacturing facilities, restaurants, etc.) perform any special cleaning or sanitation procedures for COVID-19?',
    'CDC recommends routine cleaning of all frequently touched surfaces in the workplace, such as workstations, countertops, and doorknobs. Use the cleaning agents that are usually used in these areas and follow the directions on the label. CDC does not recommend any additional disinfection beyond routine cleaning at this time. ',

    'What is the FDA doing to respond to foodborne illnesses during the COVID-19 pandemic?',
    ' The virus that causes COVID-19 is a virus that causes respiratory illness. Viruses like norovirus and hepatitis A that can make people sick through contaminated food usually cause gastrointestinal or stomach illness. Currently there is no evidence of food, food containers, or food packaging being associated with transmission of COVID-19.  ',

    'Can people get COVID-19 from pets or other animals?',
    'Based on the information available to date, the risk of pets or other animals spreading COVID-19 to people is considered to be low. ',
    'Can pets or other animals get COVID-19 from people?',
    'The virus that causes COVID-19 can spread from people to animals including pets, zoo animals and wildlife and may spread to other animals, especially during close contact. If a person inside the household becomes sick, isolate that person from everyone else, including pets and other animals.',

    'Should I get my pet tested for COVID-19?',
    'outine testing of pets for COVID-19 is not recommended at this time. There is currently no evidence that pets are a source of COVID-19 infection people in the U.S. Based on the limited information available to date, the risk of pets spreading the ',

    'What animal species can get COVID-19?',
    '          Although we know certain bacteria and fungi can be carried on fur and hair, there is no evidence that viruses, including the virus that causes COVID-19, can spread to people from the skin, fur, or hair of pets.',

    'Can pets carry the virus that causes COVID-19 on their skin or fur?',
    'Although we know certain bacteria and fungi can be carried on fur and hair, there is no evidence that viruses, including the virus that causes COVID-19, can spread to people from the skin, fur, or hair of pets.',

    'Are there any approved products that can prevent or treat COVID-19 in animals?',
    'No. Under the Federal Food, Drug',
    'Are there shortages or disruptions to the U.S. pet food supply? ',
    'In general, pet food is available. There may be intermittent decreased availability of certain brands/flavors, but there has been and continues to be product available to meet pets’ nutritional needs.',
    ' Are there any animal drug shortages due to the COVID-19 outbreak?',
    'The FDA has been and is continuing to closely monitor how the COVID-19 outbreak may impact the animal medical product supply chain.',
]

trainer = ListTrainer(bot)
trainer.train(convo)


app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    answer_from_bot = bot.get_response(query)
    engine.say(answer_from_bot)
    return str(answer_from_bot)


if __name__ == "__main__":
    app.run(port=8000, debug=True)