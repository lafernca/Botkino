from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

enfermedades_info = {
    "anemia por deficiencia de hierro": {
        "causas": "La anemia por deficiencia de hierro suele ocurrir cuando el cuerpo no tiene suficiente hierro para producir hemoglobina, la proteína en los glóbulos rojos que transporta oxígeno a los tejidos del cuerpo. Las causas pueden incluir pérdida de sangre debido a menstruación abundante, problemas gastrointestinales como úlceras o enfermedad inflamatoria intestinal, mala absorción de hierro debido a condiciones como enfermedad celíaca o cirugía gástrica, o dietas pobres en hierro, como la dieta vegetariana.",
        "tratamiento": "El tratamiento principal para la anemia por deficiencia de hierro implica la suplementación con hierro, generalmente en forma de sales de hierro por vía oral. Esto puede incluir preparaciones de sulfato ferroso u otros compuestos de hierro. Su médico determinará la dosis adecuada y la duración del tratamiento según su nivel de deficiencia y respuesta al tratamiento. Si no responde al tratamiento con hierro o experimenta efectos secundarios, es importante comunicarse con su médico. Pueden ser necesarias pruebas adicionales para identificar la causa subyacente de la anemia o ajustar el plan de tratamiento. En algunos casos, puede ser necesario considerar opciones de tratamiento alternativas, como la administración de hierro por vía intravenosa. Su médico puede guiarlo en las mejores opciones para su situación individual.",
        "diagnostico": "Los síntomas de la anemia por deficiencia de hierro pueden incluir fatiga, debilidad, palidez, falta de aire, mareos, dolores de cabeza y palpitaciones cardíacas. Su médico puede realizar pruebas de laboratorio, como análisis de sangre para medir los niveles de hemoglobina, hierro y ferritina, así como exámenes físicos para evaluar los síntomas y posibles fuentes de pérdida de sangre.",
        "mejora": "Por lo general, se espera ver una mejora en los niveles de hemoglobina dentro de las tres semanas de iniciar el tratamiento con hierro. Sin embargo, la reposición completa de los depósitos de hierro en el cuerpo puede llevar varios meses. Es importante seguir las recomendaciones de su médico y completar el curso completo de tratamiento."
    },
    "talasemia beta": {
        "causas": "La talasemia beta es una enfermedad en la cual hay una disminución o ausencia en la producción de una o más cadenas de globina, lo que resulta en una producción desequilibrada de estas cadenas. Este desequilibrio lleva a la formación de tetrameros y precipitación dentro de los glóbulos rojos, lo que causa una apoptosis crónica en la médula ósea y hemólisis crónica en la sangre periférica. Esto puede llevar a anemia crónica y otros síntomas. Los síntomas pueden variar dependiendo de la gravedad de la condición. En los casos más graves, como la talasemia beta mayor, los síntomas pueden incluir anemia severa, hepatomegalia (aumento del tamaño del hígado), esplenomegalia (aumento del tamaño del bazo), deformidades esqueléticas y retraso en el crecimiento. En formas menos graves, como la talasemia beta intermedia, los síntomas pueden ser menos severos.",
        "tratamiento": "El tratamiento depende de la gravedad de la condición. En casos graves, como la talasemia beta mayor, puede ser necesario recibir transfusiones de sangre regulares para mantener los niveles de hemoglobina dentro de un rango seguro. Además, pueden ser necesarios tratamientos para manejar la sobrecarga de hierro, como quelantes de hierro. En casos menos graves, el tratamiento puede centrarse en el manejo de los síntomas y la prevención de complicaciones.",
        "diagnostico": "El diagnóstico de la talasemia beta se realiza mediante pruebas de laboratorio, como análisis de sangre para medir los niveles de hemoglobina y otros parámetros sanguíneos, así como pruebas genéticas para identificar mutaciones en los genes de la globina. También pueden ser necesarios estudios de imagen, como radiografías o resonancias magnéticas, para evaluar el tamaño del hígado, el bazo y otros órganos.",
        "mejora": "La talasemia beta es una condición crónica que requiere manejo a largo plazo. Con un tratamiento adecuado y seguimiento médico regular, muchas personas con talasemia beta pueden llevar vidas saludables y productivas. Es importante seguir las recomendaciones de su médico y mantenerse informado sobre su condición para poder tomar decisiones informadas sobre su atención médica."
    },
    "esferocitosis": {
        "causas": "La esferocitosis es una enfermedad hereditaria caracterizada por la presencia de glóbulos rojos esféricos en lugar de tener su forma habitual de disco bicóncavo. Esto puede provocar hemólisis, que es la destrucción prematura de los glóbulos rojos en el bazo. Como resultado, puedes experimentar anemia y otros síntomas asociados.",
        "tratamiento": "El tratamiento suele ser de apoyo y puede incluir suplementos de ácido fólico para ayudar a mantener la producción de glóbulos rojos. En casos graves, puede ser necesaria la extirpación del bazo (esplenectomía) para reducir la destrucción de los glóbulos rojos. Sin embargo, esta opción se reserva para pacientes con síntomas severos o complicaciones.",
        "diagnostico": "Los síntomas pueden variar desde leves hasta graves, e incluyen fatiga, debilidad, palidez, ictericia (coloración amarillenta de la piel y los ojos), agrandamiento del bazo y, en algunos casos, cálculos biliares. El diagnóstico se realiza mediante pruebas de laboratorio, como análisis de sangre y estudios de imagen, que pueden mostrar un aumento en el número de glóbulos rojos esféricos.",
        "mejora": "Algunas complicaciones comunes incluyen episodios de anemia severa (llamados crisis aplásicas), aumento del riesgo de infecciones, formación de cálculos biliares y, en casos graves, insuficiencia medular. Es importante estar atento a los síntomas y recibir atención médica adecuada para prevenir y tratar estas complicaciones. Es importante mantener una comunicación abierta con tu médico y seguir sus recomendaciones de tratamiento. Esto puede incluir tomar suplementos de ácido fólico, evitar situaciones que puedan desencadenar crisis de anemia y buscar atención médica inmediata si experimentas síntomas preocupantes. Además, es importante mantener un estilo de vida saludable, incluyendo una dieta equilibrada y ejercicio regular, para ayudar a mantener tu salud en general."
    },
    "policitemia vera": {
        "causas": "La policitemia vera es un trastorno de la sangre en el que la médula ósea produce demasiados glóbulos rojos. Esto puede llevar a un aumento en la viscosidad de la sangre, lo que aumenta el riesgo de coágulos sanguíneos y otros problemas de salud. La policitemia vera suele ser causada por una mutación genética en las células madre de la médula ósea. También puede estar asociada con la exposición a la radiación o a ciertos productos químicos, aunque esto es menos común.",
        "tratamiento": "El tratamiento puede incluir medicamentos para reducir el número de glóbulos rojos, como la hidroxiurea, y la flebotomía para extraer sangre y reducir la viscosidad. Además, es importante llevar un estilo de vida saludable, incluyendo una dieta equilibrada y ejercicio regular, y seguir de cerca las indicaciones de tu médico para controlar la enfermedad.", 
        "diagnostico": "Los síntomas pueden incluir fatiga, mareos, enrojecimiento de la piel, dificultad para respirar y dolor en el abdomen o el pecho. El diagnóstico se realiza mediante análisis de sangre para detectar niveles elevados de glóbulos rojos y una mutación genética llamada JAK2-V617F.",
        "mejora": "Las complicaciones pueden incluir coágulos sanguíneos, accidentes cerebrovasculares, problemas cardíacos, como ataques cardíacos, y problemas de sangrado debido a la viscosidad aumentada de la sangre. Es importante recibir tratamiento para prevenir estas complicaciones."
    },
    "células falciformes": {
        "causas": "La anemia de células falciformes es un trastorno sanguíneo en el que los glóbulos rojos tienen una forma anormal en forma de hoz. Esto puede causar obstrucciones en los vasos sanguíneos, lo que lleva a dolor intenso, daño en órganos y otras complicaciones de salud. Los síntomas pueden variar desde dolor intenso en las articulaciones, huesos y músculos hasta complicaciones graves como accidentes cerebrovasculares, infecciones frecuentes y daño en órganos como los riñones o el corazón. El manejo suele implicar el control del dolor, la prevención de infecciones y el monitoreo regular de la salud.",
        "tratamiento": "El tratamiento puede incluir medicamentos para controlar el dolor, prevenir infecciones y reducir el riesgo de complicaciones graves. También es importante recibir atención médica regular para monitorear la salud y ajustar el tratamiento según sea necesario.",
        "diagnostico": "Para diagnosticar este tipo de anemia, se realizan pruebas de laboratorio como un hemograma completo y un frotis de sangre periférica para observar los glóbulos rojos. Las pruebas específicas incluyen la electroforesis de hemoglobina para identificar la hemoglobina S (HbS) y la prueba de solubilidad de la hemoglobina. El diagnóstico prenatal se puede realizar mediante amniocentesis o muestreo de vellosidades coriónicas para detectar el gen de la enfermedad en el feto. Pruebas genéticas, como la secuenciación del ADN, identifican mutaciones en el gen HBB. En muchos países, se realiza un tamizaje neonatal a todos los recién nacidos para detectar hemoglobina S. Un diagnóstico precoz y un seguimiento regular son esenciales para manejar los síntomas y complicaciones de la enfermedad, mejorando significativamente la calidad de vida de los pacientes.",
        "mejora": "Es importante mantenerse bien hidratado, evitar cambios bruscos de temperatura y evitar situaciones que puedan desencadenar crisis de dolor, como el estrés o la deshidratación. Además, seguir las recomendaciones médicas, como tomar ácido fólico y recibir vacunas, puede ayudar a prevenir complicaciones. Las complicaciones pueden incluir crisis de dolor intenso, problemas respiratorios graves como el síndrome torácico agudo, riesgo aumentado de infecciones, accidentes cerebrovasculares, problemas oculares, renales y hepáticos, así como problemas en el crecimiento y desarrollo, entre otros."
    },
    "anemia hemolítica": {
        "causas": "La anemia hemolítica es una condición en la que los glóbulos rojos se destruyen más rápido de lo normal, lo que lleva a una disminución en la cantidad de glóbulos rojos en la sangre. Esto puede causar síntomas como fatiga, dificultad para respirar y cambios en el color de la orina debido a la liberación de hemoglobina. Además, puede afectar la capacidad de transporte de oxígeno de tu cuerpo. La anemia hemolítica puede ser hereditaria o adquirida. Las causas hereditarias incluyen trastornos de la membrana de los glóbulos rojos, deficiencias enzimáticas y anormalidades en la hemoglobina. Las causas adquiridas pueden ser inmunes, como la hemólisis autoinmune, o no inmunes, como la hemólisis asociada a infecciones o trastornos como el síndrome urémico hemolítico.",
        "tratamiento": "El tratamiento depende de la causa subyacente de la anemia hemolítica. Esto puede implicar el tratamiento de la enfermedad subyacente, como infecciones o trastornos autoinmunes, así como la suplementación con ácido fólico y hierro si es necesario. En algunos casos, puede ser necesaria la transfusión de glóbulos rojos.",
        "diagnostico": "Los síntomas pueden incluir fatiga, palidez, dificultad para respirar y orina de color oscuro debido a la presencia de hemoglobina liberada. El diagnóstico se realiza mediante pruebas de laboratorio que pueden incluir análisis de sangre, como un hemograma completo y un frotis de sangre periférica, así como pruebas para medir los niveles de bilirrubina y otras enzimas.",
        "mejora": "Es importante seguir las recomendaciones de tu médico y tomar cualquier medicamento recetado según las indicaciones. Además, mantener una dieta saludable rica en hierro y ácido fólico puede ser beneficioso. También es importante evitar factores que puedan desencadenar la hemólisis, como ciertos medicamentos o infecciones, y mantenerse bien hidratado."
    },
    "deficiencia de la vitamina B12": {
        "causas": "La deficiencia de vitamina B12 es una condición en la que el cuerpo no tiene suficiente vitamina B12 para funcionar correctamente. Esto puede llevar a una anemia megaloblástica, que es una condición en la que los glóbulos rojos son más grandes de lo normal y no pueden funcionar correctamente. Además, la falta de vitamina B12 puede causar síntomas neurológicos como hormigueo en las extremidades y problemas de equilibrio. Las causas pueden incluir trastornos autoinmunes como la anemia perniciosa, enfermedades del intestino delgado como la enfermedad de Crohn, y ciertos medicamentos que pueden interferir con la absorción de vitamina B12. Además, una dieta pobre en alimentos que contienen vitamina B12, como carne, pescado, huevos y productos lácteos, también puede provocar deficiencia.",
        "tratamiento": "El tratamiento generalmente implica la administración de suplementos de vitamina B12, ya sea por vía oral o mediante inyecciones intramusculares. En casos graves o cuando la absorción de vitamina B12 está comprometida, pueden ser necesarias inyecciones frecuentes de vitamina B12. Además, es importante identificar y tratar cualquier causa subyacente de la deficiencia de vitamina B12.",
        "diagnostico": "La deficiencia de vitamina B12 se diagnostica mediante pruebas de laboratorio que pueden incluir análisis de sangre para medir los niveles de vitamina B12 en suero. Además, se pueden realizar pruebas adicionales, como un hemograma completo y un frotis de sangre periférica, para evaluar los cambios en los glóbulos rojos. Los síntomas pueden incluir fatiga, dificultad para respirar, hormigueo en las extremidades y problemas de equilibrio. También puede haber síntomas neurológicos como cambios en la sensibilidad y la vibración en las extremidades. En casos graves, la deficiencia de vitamina B12 puede causar daño permanente a la médula espinal.",
        "mejora": "Para manejar la deficiencia de vitamina B12 y mejorar tu calidad de vida, puedes seguir varios pasos: tomar suplementos de vitamina B12, ya sea en forma de inyecciones o pastillas según la recomendación médica, y tratar cualquier condición subyacente como anemia perniciosa o enfermedades gastrointestinales. Además, incluye en tu dieta alimentos ricos en vitamina B12, como carnes, aves, pescados, huevos, productos lácteos y alimentos fortificados, especialmente si sigues una dieta vegetariana o vegana. Adopta hábitos de vida saludables como limitar el consumo de alcohol y dejar de fumar, ya que estos pueden interferir con la absorción de la vitamina. Realiza chequeos médicos regulares para monitorear tus niveles de vitamina B12 y ajustar el tratamiento según sea necesario, y presta atención a los síntomas de deficiencia."
    },
    "cirrosis": {
        "causas": "La cirrosis es una etapa avanzada de la fibrosis hepática que causa cambios en la estructura normal del hígado. Esto puede llevar a la formación de cicatrices en el hígado, lo que dificulta su funcionamiento adecuado. La cirrosis puede causar síntomas como fatiga, pérdida de peso y complicaciones graves como hipertensión portal y ascitis. Las causas más comunes de cirrosis incluyen el consumo crónico de alcohol, la hepatitis viral crónica (como la hepatitis B y C) y la esteatohepatitis metabólica (anteriormente conocida como esteatohepatitis no alcohólica). También puede ser causada por enfermedades biliares, como la colangitis biliar primaria y la colangitis esclerosante primaria.",
        "tratamiento": "El tratamiento se centra en controlar los síntomas y tratar las complicaciones. Esto puede incluir cambios en el estilo de vida, como evitar el alcohol y mantener una dieta saludable. En algunos casos, puede ser necesario el trasplante de hígado. Además, se pueden utilizar medicamentos para tratar complicaciones como la hipertensión portal y la encefalopatía hepática. Es importante seguir las recomendaciones de su médico y asistir a controles regulares para monitorear la progresión de la enfermedad. Los síntomas pueden ser vagos y no específicos en las etapas tempranas, pero pueden incluir fatiga, pérdida de apetito y sensación de malestar general. A medida que la cirrosis avanza, pueden aparecer complicaciones como hipertensión portal, ascitis (acumulación de líquido en el abdomen), encefalopatía hepática y sangrado gastrointestinal.",
        "diagnostico": "El diagnóstico generalmente se realiza mediante pruebas de laboratorio, como análisis de sangre y pruebas de función hepática. Además, se pueden realizar pruebas de imagen, como ecografías o resonancias magnéticas, para evaluar la estructura del hígado. En algunos casos, puede ser necesario realizar una biopsia hepática para confirmar el diagnóstico.",
        "mejora": "Para manejar la cirrosis y mejorar tu calidad de vida, es fundamental seguir el tratamiento médico prescrito, que puede incluir medicamentos para controlar síntomas y complicaciones, así como posibles intervenciones para tratar causas subyacentes como hepatitis o alcoholismo; adoptar una dieta baja en sodio para reducir la retención de líquidos y evitar el consumo de alcohol, que puede empeorar la enfermedad; mantener un peso saludable y evitar alimentos grasos para no sobrecargar el hígado; realizar actividad física moderada para mejorar la salud general; vacunarse contra hepatitis A y B, gripe y neumonía para prevenir infecciones; asistir a consultas médicas regulares para monitorear la progresión de la enfermedad y ajustar el tratamiento; y considerar unirse a grupos de apoyo para obtener apoyo emocional y compartir experiencias con otros en situaciones similares. Además, es crucial evitar el uso de medicamentos que pueden ser tóxicos para el hígado y consultar siempre a un médico antes de tomar cualquier nuevo medicamento o suplemento."
    },
    "deficiencia de piruvato quinasa": {
        "causas": "La deficiencia de piruvato quinasa es un trastorno hereditario que causa anemia hemolítica, lo que significa que tus glóbulos rojos se destruyen más rápidamente de lo normal. Esto ocurre debido a una deficiencia de una enzima llamada piruvato quinasa, que es importante para el funcionamiento normal de tus glóbulos rojos. Como resultado, tus glóbulos rojos pueden ser menos estables y tener dificultades para producir suficiente energía.",
        "tratamiento": "El tratamiento depende de la gravedad de los síntomas. Se pueden recomendar medidas de apoyo, como tomar ácido fólico diariamente y, en casos graves, puede ser necesario recibir transfusiones sanguíneas. En algunos casos, la extirpación del bazo (esplenectomía) puede ser beneficiosa para reducir la necesidad de transfusiones. Durante una crisis aplásica, es importante recibir tratamiento de apoyo mientras el cuerpo se recupera.",
        "diagnostico": "El diagnóstico generalmente se realiza mediante análisis de sangre para evaluar el conteo de glóbulos rojos y otros parámetros sanguíneos. También se pueden realizar pruebas específicas para medir los niveles de la enzima piruvato quinasa en tus glóbulos rojos. Además, se pueden realizar otras pruebas para descartar otras causas de anemia hemolítica. Los síntomas pueden variar mucho, pero comúnmente incluyen fatiga, palidez, dificultad para respirar, ictericia (coloración amarillenta de la piel y los ojos) y agrandamiento del bazo. Estos síntomas pueden aparecer desde el nacimiento o manifestarse más adelante en la vida.",
        "mejora": "Una complicación importante es la crisis aplásica, que puede ocurrir durante infecciones virales como la causada por el parvovirus B19. Esto puede llevar a una disminución drástica en la producción de glóbulos rojos y requerir medidas de apoyo, como transfusiones sanguíneas."
    },
    "deficiencia de ácido fólico": {
        "causas": "La deficiencia de ácido fólico es una condición en la que el cuerpo no tiene suficiente cantidad de esta vitamina B. El ácido fólico es importante para la producción normal de glóbulos rojos y para la síntesis del ADN. Cuando hay deficiencia de ácido fólico, puede ocurrir una anemia megaloblástica, que se caracteriza por glóbulos rojos anormalmente grandes y pocos en número. Esto puede causar fatiga, debilidad y otros síntomas asociados con la anemia. La deficiencia de ácido fólico puede ser causada por una variedad de factores, que incluyen una dieta pobre en alimentos ricos en folato, como verduras de hoja verde, hígado y nueces. Además, ciertas condiciones médicas, como la enfermedad celíaca, la enfermedad de Crohn y la diálisis renal, pueden interferir con la absorción adecuada de ácido fólico. El consumo excesivo de alcohol y ciertos medicamentos también puede contribuir a la deficiencia de ácido fólico.",
        "tratamiento": "El tratamiento principal para la deficiencia de ácido fólico implica tomar suplementos de ácido fólico por vía oral. La dosis típica es de 5 mg al día. Sin embargo, es importante tener en cuenta que nunca se debe tratar la deficiencia de ácido fólico sola si también hay deficiencia de vitamina B12, ya que esto podría empeorar los síntomas.",
        "diagnostico": "El diagnóstico de deficiencia de ácido fólico generalmente se realiza mediante análisis de sangre para medir los niveles de folato en suero y en glóbulos rojos. Estas pruebas pueden ayudar a determinar si sus niveles de ácido fólico son bajos y si necesita tratamiento.",
        "mejora": "Para mejorar la deficiencia de ácido fólico, consume alimentos ricos en esta vitamina, como vegetales de hoja verde, frutas cítricas, legumbres, y cereales fortificados; toma suplementos de ácido fólico según la recomendación de tu médico; evita el consumo excesivo de alcohol, que puede interferir con la absorción de folato; y realiza chequeos médicos regulares para monitorear tus niveles y ajustar el tratamiento si es necesario. Para prevenir la deficiencia de ácido fólico, es importante consumir una dieta equilibrada que incluya alimentos ricos en folato, como verduras de hoja verde, hígado, nueces y levadura. Además, en ciertas situaciones, como el embarazo o en casos de aumento de la demanda de ácido fólico, puede ser recomendable tomar suplementos de ácido fólico como medida preventiva."
    }
    }

class ActionConfirmarEnfermedad(Action):
    def name(self) -> Text:
        return "action_confirmar_enfermedad"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        enfermedad = tracker.latest_message['entities'][0]['value']
        dispatcher.utter_message(template="utter_confirmar_enfermedad", enfermedad=enfermedad)
        return [SlotSet("enfermedad", enfermedad)]

class ActionResponderCausas(Action):
    def name(self) -> Text:
        return "action_responder_causas"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        enfermedad = tracker.get_slot("enfermedad")
        if enfermedad in enfermedades_info:
            dispatcher.utter_message(text=enfermedades_info[enfermedad]["causas"])
        else:
            dispatcher.utter_message(template="utter_responder_causas_default", enfermedad=enfermedad)
        return []

class ActionResponderTratamiento(Action):
    def name(self) -> Text:
        return "action_responder_tratamiento"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        enfermedad = tracker.get_slot("enfermedad")
        if enfermedad in enfermedades_info:
            dispatcher.utter_message(text=enfermedades_info[enfermedad]["tratamiento"])
        else:
            dispatcher.utter_message(template="utter_responder_tratamiento_default", enfermedad=enfermedad)
        return []

class ActionResponderDiagnostico(Action):
    def name(self) -> Text:
        return "action_responder_diagnostico"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        enfermedad = tracker.get_slot("enfermedad")
        if enfermedad in enfermedades_info:
            dispatcher.utter_message(text=enfermedades_info[enfermedad]["diagnostico"])
        else:
            dispatcher.utter_message(template="utter_responder_diagnostico_default", enfermedad=enfermedad)
        return []

class ActionResponderMejora(Action):
    def name(self) -> Text:
        return "action_responder_mejora"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        enfermedad = tracker.get_slot("enfermedad")
        if enfermedad in enfermedades_info:
            dispatcher.utter_message(text=enfermedades_info[enfermedad]["mejora"])
        else:
            dispatcher.utter_message(template="utter_responder_mejora_default", enfermedad=enfermedad)
        return []