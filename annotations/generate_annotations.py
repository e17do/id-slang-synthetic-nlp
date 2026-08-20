import json
from pathlib import Path


# ============================================================
# id-slang-synthetic-nlp
# Automated Dataset Annotation Generator
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = ROOT / "dataset" / "dataset_slang_indonesia.json"
REGIONAL_PATH = ROOT / "linguistic_clusters" / "regional_clusters.json"
TAXONOMY_PATH = ROOT / "linguistic_taxonomy" / "taxonomy.json"
OUTPUT_PATH = ROOT / "annotations" / "record_annotations.json"


# ============================================================
# Utility
# ============================================================

def load_json(path):
    if not path.exists():
        raise FileNotFoundError(
            f"Required file not found: {path}"
        )

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize(text):
    return str(text).lower().strip()


def build_lookup(items, id_field="id"):
    """
    Build lookup table using a configurable identifier field.

    Taxonomy items use:
        id

    Regional cluster items use:
        cluster_id
    """

    return {
        item[id_field]: item
        for item in items
        if isinstance(item, dict)
        and id_field in item
    }


# ============================================================
# Domain Detection
# ============================================================

def detect_domain(text, slang):

    text = normalize(text)
    slang = normalize(slang)

    rules = {

        "DOMAIN-GAMING": [
            "gaming",
            "game",
            "rank",
            "ranked",
            "mabar",
            "push rank",
            "player",
            "server",
            "lobby",
            "match",
            "clutch",
            "noob",
            "carry",
            "buff",
            "nerf",
            "afk",
            "gg",
            "win",
            "lose"
        ],

        "DOMAIN-FINTECH": [
            "paylater",
            "pinjol",
            "e-wallet",
            "ewallet",
            "dompet digital",
            "transfer",
            "saldo",
            "qris",
            "fintech",
            "cicilan",
            "tagihan"
        ],

        "DOMAIN-CRYPTO": [
            "crypto",
            "bitcoin",
            "btc",
            "ethereum",
            "eth",
            "token",
            "coin",
            "rugpull",
            "to the moon",
            "serok bawah",
            "altcoin",
            "trading"
        ],

        "DOMAIN-FINANCE": [
            "cuan",
            "boncos",
            "investasi",
            "saham",
            "tabungan",
            "gaji",
            "financial freedom",
            "frugal living",
            "budget",
            "keuangan",
            "sandwich generation"
        ],

        "DOMAIN-WORK": [
            "office",
            "kantor",
            "meeting",
            "deadline",
            "kerja",
            "work",
            "bos",
            "atasan",
            "client",
            "freelance",
            "startup",
            "remote",
            "wfh",
            "career",
            "karier"
        ],

        "DOMAIN-EDUCATION": [
            "kampus",
            "kuliah",
            "sekolah",
            "dosen",
            "mahasiswa",
            "ujian",
            "tugas",
            "skripsi",
            "kelas",
            "belajar"
        ],

        "DOMAIN-TECH": [
            "coding",
            "programming",
            "software",
            "hardware",
            "ai",
            "artificial intelligence",
            "laptop",
            "app",
            "aplikasi",
            "developer",
            "bug"
        ],

        "DOMAIN-ECOMMERCE": [
            "checkout",
            "marketplace",
            "shopee",
            "tokopedia",
            "diskon",
            "promo",
            "seller",
            "buyer",
            "ongkir",
            "belanja online"
        ],

        "DOMAIN-DATING": [
            "dating",
            "gebetan",
            "pacar",
            "crush",
            "pdkt",
            "date",
            "relationship",
            "red flag",
            "green flag",
            "ghosting",
            "ghosted"
        ],

        "DOMAIN-ENTERTAINMENT": [
            "film",
            "movie",
            "series",
            "drakor",
            "musik",
            "konser",
            "idol",
            "fandom",
            "lagu",
            "artis"
        ],

        "DOMAIN-FOOD": [
            "makan",
            "kuliner",
            "kopi",
            "ngopi",
            "resto",
            "restaurant",
            "warung",
            "food",
            "nasi",
            "jajan"
        ],

        "DOMAIN-LIFESTYLE": [
            "travel",
            "liburan",
            "fashion",
            "outfit",
            "gym",
            "workout",
            "healing",
            "lifestyle",
            "skincare"
        ],

        "DOMAIN-MEME": [
            "meme",
            "wkwk",
            "lol",
            "bjir",
            "bro",
            "core",
            "viral"
        ]
    }

    for domain, keywords in rules.items():

        if any(
            keyword in text or keyword in slang
            for keyword in keywords
        ):
            return domain

    return "DOMAIN-SOCIAL"


# ============================================================
# Generation Detection
# ============================================================

def detect_generation(text, slang):

    text = normalize(text)
    slang = normalize(slang)

    alpha_markers = [
        "skibidi",
        "sigma",
        "gyatt",
        "rizz",
        "gwenchana",
        "sus",
        "npc"
    ]

    genz_markers = [
        "fomo",
        "yolo",
        "core",
        "slay",
        "valid",
        "spill",
        "relate",
        "gas",
        "menyala",
        "bjir",
        "gabut",
        "cees"
    ]

    millennial_markers = [
        "work",
        "office",
        "meeting",
        "deadline",
        "healing",
        "financial freedom",
        "frugal living"
    ]

    if any(
        marker in text or marker in slang
        for marker in alpha_markers
    ):
        return "GEN-ALPHA"

    if any(
        marker in text or marker in slang
        for marker in genz_markers
    ):
        return "GEN-Z"

    if any(
        marker in text or marker in slang
        for marker in millennial_markers
    ):
        return "GEN-MILLENNIAL"

    return "GEN-CROSS"


# ============================================================
# Register Detection
# ============================================================

def detect_register(text, sentiment):

    text = normalize(text)
    sentiment = normalize(sentiment)

    if any(
        x in sentiment
        for x in [
            "sindiran",
            "sarcas"
        ]
    ):
        return "REG-SARCASTIC"

    if any(
        x in sentiment
        for x in [
            "humor",
            "terhibur"
        ]
    ):
        return "REG-HUMOR"

    if any(
        x in sentiment
        for x in [
            "marah",
            "frustr",
            "kesal"
        ]
    ):
        return "REG-EMOTIVE"

    if any(
        x in text
        for x in [
            "office",
            "meeting",
            "deadline",
            "client",
            "bos",
            "kerja"
        ]
    ):
        return "REG-WORKPLACE"

    if any(
        x in text
        for x in [
            "twitter",
            "x ",
            "tiktok",
            "instagram",
            "viral",
            "post",
            "comment"
        ]
    ):
        return "REG-INTERNET"

    return "REG-CASUAL"


# ============================================================
# Code Switching Detection
# ============================================================

def detect_code_switching(text):

    text = normalize(text)

    english_markers = [
        " literally ",
        " actually ",
        " honestly ",
        " vibe",
        " vibes",
        "core",
        "fomo",
        "yolo",
        "deadline",
        "meeting",
        "work",
        "office",
        "client",
        "ghosted",
        "red flag",
        "green flag",
        "financial freedom",
        "frugal living",
        "to the moon",
        "paylater",
        "gaming"
    ]

    sundanese_markers = [
        "teh",
        "mah",
        "atuh",
        "ieu",
        "eta",
        "kumaha",
        "euy",
        "punten"
    ]

    javanese_markers = [
        "rek",
        "ndak",
        "ora",
        "opo",
        "piye",
        "cok",
        "cak",
        "ndeso",
        "ngene"
    ]

    minangkabau_markers = [
        "uni",
        "uda",
        "awak",
        "lai"
    ]

    makassar_markers = [
        "ji",
        "mi",
        "ki",
        "ta",
        "kodong"
    ]

    manado_markers = [
        "jo",
        "pe",
        "so",
        "kita pe"
    ]

    if any(
        x in text
        for x in english_markers
    ):
        return "CS-ID-EN"

    if any(
        x in text
        for x in sundanese_markers
    ):
        return "CS-ID-SUN"

    if any(
        x in text
        for x in javanese_markers
    ):
        return "CS-ID-JAV"

    if any(
        x in text
        for x in minangkabau_markers
    ):
        return "CS-ID-MIN"

    if any(
        x in text
        for x in makassar_markers
    ):
        return "CS-ID-MKS"

    if any(
        x in text
        for x in manado_markers
    ):
        return "CS-ID-MAN"

    return "CS-NONE"


# ============================================================
# Regional Cluster Detection
# ============================================================

def detect_regional_cluster(location):

    location = normalize(location)

    mapping = {

        "jakarta selatan": "ID-REG-JAKSEL",
        "jakarta": "ID-REG-JKT",

        "bandung": "ID-REG-BDG",
        "cirebon": "ID-REG-CIREBON",

        "yogyakarta": "ID-REG-JOG",
        "jogja": "ID-REG-JOG",
        "solo": "ID-REG-SOLO",
        "semarang": "ID-REG-SMG",

        "surabaya": "ID-REG-SBY",
        "malang": "ID-REG-MLG",

        "medan": "ID-REG-MDN",
        "binjai": "ID-REG-BIN",
        "padang": "ID-REG-PDG",
        "palembang": "ID-REG-PLB",
        "pekanbaru": "ID-REG-PKU",

        "makassar": "ID-REG-MKS",
        "gowa": "ID-REG-GOWA",
        "manado": "ID-REG-MND",

        "banjarmasin": "ID-REG-BJM",
        "samarinda": "ID-REG-SMR",
        "denpasar": "ID-REG-DPS",

        "komunitas gaming": "ID-REG-GAMING",
        "gaming": "ID-REG-GAMING"
    }

    # Prioritize longer/more specific locations first.
    for location_name in sorted(
        mapping,
        key=len,
        reverse=True
    ):

        if location_name in location:
            return mapping[location_name]

    return "ID-REG-URBAN"


# ============================================================
# Main Generator
# ============================================================

def main():

    print("=" * 70)
    print("id-slang-synthetic-nlp")
    print("AUTOMATED DATASET ANNOTATION GENERATOR")
    print("=" * 70)

    # --------------------------------------------------------
    # Load source files
    # --------------------------------------------------------

    dataset = load_json(DATASET_PATH)
    regional = load_json(REGIONAL_PATH)
    taxonomy = load_json(TAXONOMY_PATH)

    if not isinstance(dataset, list):
        raise ValueError(
            "Dataset root harus berupa JSON array."
        )

    if not isinstance(regional, dict):
        raise ValueError(
            "regional_clusters.json harus berupa JSON object."
        )

    if not isinstance(
        regional.get("clusters"),
        list
    ):
        raise ValueError(
            "regional_clusters.json tidak memiliki "
            "array 'clusters'."
        )

    if not isinstance(taxonomy, dict):
        raise ValueError(
            "taxonomy.json harus berupa JSON object."
        )

    # --------------------------------------------------------
    # Build regional cluster lookup
    #
    # IMPORTANT:
    # regional_clusters.json uses "cluster_id",
    # not "id".
    # --------------------------------------------------------

    regional_lookup = build_lookup(
        regional["clusters"],
        id_field="cluster_id"
    )

    regional_ids = set(
        regional_lookup.keys()
    )

    # --------------------------------------------------------
    # Build taxonomy lookup
    #
    # Taxonomy uses "id".
    # --------------------------------------------------------

    taxonomy_ids = set()

    dimensions = taxonomy.get(
        "dimensions",
        {}
    )

    if not isinstance(dimensions, dict):
        raise ValueError(
            "taxonomy.json field 'dimensions' "
            "harus berupa object."
        )

    for dimension_name, dimension_items in dimensions.items():

        if not isinstance(
            dimension_items,
            list
        ):
            raise ValueError(
                f"Taxonomy dimension '{dimension_name}' "
                "harus berupa array."
            )

        taxonomy_ids.update(
            build_lookup(
                dimension_items,
                id_field="id"
            ).keys()
        )

    # --------------------------------------------------------
    # Generate annotations
    # --------------------------------------------------------

    annotations = []
    seen_ids = set()

    for index, record in enumerate(
        dataset,
        start=1
    ):

        if not isinstance(record, dict):
            raise ValueError(
                f"Dataset record #{index} bukan object JSON."
            )

        required_fields = [
            "id",
            "konteks_percakapan",
            "ragam_slang",
            "sentimen_emosi",
            "lokasi_dominan"
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in record
        ]

        if missing_fields:
            raise ValueError(
                f"Dataset record #{index} "
                f"missing fields: {missing_fields}"
            )

        record_id = record["id"]

        if record_id in seen_ids:
            raise ValueError(
                f"Duplicate dataset ID detected: "
                f"{record_id}"
            )

        seen_ids.add(record_id)

        text = record[
            "konteks_percakapan"
        ]

        slang = record[
            "ragam_slang"
        ]

        sentiment = record[
            "sentimen_emosi"
        ]

        location = record[
            "lokasi_dominan"
        ]

        # ----------------------------------------------------
        # Detect annotation dimensions
        # ----------------------------------------------------

        regional_cluster = (
            detect_regional_cluster(
                location
            )
        )

        domain = detect_domain(
            text,
            slang
        )

        generation = detect_generation(
            text,
            slang
        )

        register = detect_register(
            text,
            sentiment
        )

        code_switching = (
            detect_code_switching(
                text
            )
        )

        annotation = {
            "id": record_id,
            "regional_cluster": regional_cluster,
            "domain": domain,
            "generation": generation,
            "register": register,
            "code_switching": code_switching
        }

        # ----------------------------------------------------
        # Validate generated regional cluster
        # ----------------------------------------------------

        if regional_cluster not in regional_ids:

            raise ValueError(
                "Unknown regional cluster: "
                f"{regional_cluster}"
            )

        # ----------------------------------------------------
        # Validate generated taxonomy IDs
        # ----------------------------------------------------

        taxonomy_fields = [
            "domain",
            "generation",
            "register",
            "code_switching"
        ]

        for field in taxonomy_fields:

            value = annotation[field]

            if value not in taxonomy_ids:

                raise ValueError(
                    f"Unknown taxonomy ID "
                    f"for {field}: {value}"
                )

        annotations.append(
            annotation
        )

    # --------------------------------------------------------
    # Ensure output directory exists
    # --------------------------------------------------------

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Write generated annotation file
    # --------------------------------------------------------

    OUTPUT_PATH.write_text(
        json.dumps(
            annotations,
            ensure_ascii=False,
            indent=2
        ) + "\n",
        encoding="utf-8"
    )

    # --------------------------------------------------------
    # Final report
    # --------------------------------------------------------

    print()
    print("Generation completed successfully.")
    print()
    print(
        f"Dataset records : {len(dataset)}"
    )

    print(
        f"Annotations     : {len(annotations)}"
    )

    print(
        f"Regional IDs     : {len(regional_ids)}"
    )

    print(
        f"Taxonomy IDs     : {len(taxonomy_ids)}"
    )

    print(
        f"Output           : {OUTPUT_PATH}"
    )

    print()
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
