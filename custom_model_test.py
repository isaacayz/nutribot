import cohere
import constant
from cohere.custom_model_dataset import InMemoryDataset  
co = cohere.Client(constant.api_key)  
def trainer():
    dataset = InMemoryDataset(training_data=[  
        (1,5),  
        (2,6),
        (3,7),
        (4,8),
        (5,9),
        (6,10),
        (7,11),
        (8,12),
        (9,13),
        (10,14),
        (11,15),
        (12,16),
        (13,17),
        (14,18),
        (15,19),
        (16,20),
        (17,21),
        (18,22),
        (19,23),
        (20,24),
        (21,25),
        (22,26),
        (23,27),
        (24,28),
        (25,29),
        (26,30),
        (27,31),
        (28,32),
        (29,33),
        (30,34),
        (31,35),
        (32,35),
    ])  
    model = co.create_custom_model("prompt-completion-ft", dataset=dataset, model_type="GENERATIVE")

trainer()