from __future__ import annotations

from mteb.abstasks import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class SlovakSentimentClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="SlovakSentimentClassification",
        description="An Slovak dataset for sentiment classification.",
        reference="https://arxiv.org/abs/2009.08712",
        dataset={
            "path": "sepidmnorozy/Slovak_sentiment",
            "revision": "e698d1df52766d73ae1cc569dfc622527c329a08",
        },
        type="Classification",
        category="s2s",
        date=("2022-01-01", "2022-01-01"),
        eval_splits=["validation", "test"],
        eval_langs=["slk-Latn"],
        main_score="accuracy",
        form=["written"],
        domains=["Reviews"],
        task_subtypes=["Sentiment/Hate speech"],
        license="Not specified",
        socioeconomic_status="mixed",
        annotations_creators="human-annotated",
        dialect=[],
        text_creation="found",
        bibtex_citation="""@inproceedings{mollanorozy-etal-2023-cross,
    title = "Cross-lingual Transfer Learning with \{P\}ersian",
    author = "Mollanorozy, Sepideh  and
      Tanti, Marc  and
      Nissim, Malvina",
    editor = "Beinborn, Lisa  and
      Goswami, Koustava  and
      Murado{\\u{g}}lu, Saliha  and
      Sorokin, Alexey  and
      Kumar, Ritesh  and
      Shcherbakov, Andreas  and
      Ponti, Edoardo M.  and
      Cotterell, Ryan  and
      Vylomova, Ekaterina",
    booktitle = "Proceedings of the 5th Workshop on Research in Computational Linguistic Typology and Multilingual NLP",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.sigtyp-1.9",
    doi = "10.18653/v1/2023.sigtyp-1.9",
    pages = "89--95",
}
""",
        n_samples={"validation": 522, "test": 1042},
        avg_character_length={"validation": 85.0, "test": 92.0},
    )
