from __future__ import annotations

from mteb.abstasks import AbsTaskSummarization
from mteb.abstasks.TaskMetadata import TaskMetadata


class ERRNewsSummarization(AbsTaskSummarization):
    metadata = TaskMetadata(
        name="ERRNews",
        description="News Article Summary Summarization dataset from ERR News broadcasts.",
        reference="https://github.com/Yale-LILY/SummEval",
        dataset={
            "path": "TalTechNLP/ERRnews",
            "revision": "9d9cb89a4c154fc81b28fbafdfa00e9a2e08835a",
        },
        type="Summarization",
        category="p2p",
        eval_splits=["test"],
        eval_langs=["est-Latn"],
        main_score="cosine_spearman",
        date=("2023-03-10", "2023-03-10"),
        form=["spoken", "written"],
        domains=["News"],
        task_subtypes="Discourse coherence",
        license="CC-by-4.0",
        socioeconomic_status="mixed",
        annotations_creators="derived",
        dialect=[],
        text_creation="created",
        bibtex_citation="""article{henryabstractive,
          title={Abstractive Summarization of Broadcast News Stories for {Estonian}},
          author={Henry, H{\"a}rm and Tanel, Alum{\"a}e},
          journal={Baltic J. Modern Computing},
          volume={10},
          number={3},
          pages={511-524},
          year={2022}
        }
        """,
        n_samples=None,
        avg_character_length=None,
    )

    @property
    def metadata_dict(self) -> dict[str, str]:
        metadata_dict = super().metadata_dict
        metadata_dict["min_score"] = 0
        metadata_dict["max_score"] = 5

        return metadata_dict
