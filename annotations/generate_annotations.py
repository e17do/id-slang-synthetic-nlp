import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = ROOT / "dataset" / "dataset_slang_indonesia.json"
REGIONAL_PATH = ROOT / "linguistic_clusters" / "regional_clusters.json"
TAXONOMY_PATH = ROOT / "linguistic_taxonomy" / "taxonomy.json"
OUTPUT_PATH = ROOT / "annotations" / "record_annotations.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize(text):
    return str(text).lower().strip()


def build_lookup(items):
    return {
        item["id"]: item
        for item in items
        if isinstance(item, dict) and "id" in item
    }


def detect_domain(text, slang):
    text = normalize(text)
    slang = normalize(slang)

    rules = {
        "DOMAIN-GAMING": [
            "gaming", "game", "rank", "ranked", "mabar",
            "push rank", "player", "server", "lobby",
            "match", "clutch", "noob", "carry", "buff",
            "nerf", "afk", "gg", "win", "lose"
        ],
        "DOMAIN-FINTECH": [
            "paylater", "pinjol", "e-wallet", "ewallet",
            "dompet digital", "transfer", "saldo", "qris",
            "fintech", "cicilan", "tagihan"
        ],
        "DOMAIN-CRYPTO": [
            "crypto", "bitcoin", "btc", "ethereum", "eth",
            "token", "coin", "rugpull", "to the moon",
            "serok bawah", "altcoin", "trading"
        ],
        "DOMAIN-FINANCE": [
            "cuan", "boncos", "investasi", "saham",
            "tabungan", "gaji", "financial freedom",
            "frugal living", "budget", "keuangan",
            "sandwich generation"
        ],
        "DOMAIN-WORK": [
            "office", "kantor", "meeting", "deadline",
            "kerja", "work", "bos", "atasan", "client",
            "freelance", "startup", "remote", "wfh",
            "career", "karier"
        ],
        "DOMAIN-EDUCATION": [
            "kampus", "kuliah", "sekolah", "dosen",
            "mahasiswa", "ujian", "tugas", "skripsi",
            "kelas", "belajar"
        ],
        "DOMAIN-TECH": [
            "coding", "programming", "software", "hardware",
            "ai", "artificial intelligence", "laptop",
            "app", "aplikasi", "developer", "bug"
        ],
        "DOMAIN-ECOMMERCE": [
            "checkout", "marketplace", "shopee", "tokopedia",
            "diskon", "promo", "checkout", "seller",
            "buyer", "ongkir", "belanja online"
        ],
        "DOMAIN-DATING": [
            "dating", "gebetan", "pacar", "crush",
            "pdkt", "date", "relationship", "red flag",
            "green flag", "ghosting", "ghosted"
        ],
        "DOMAIN-ENTERTAINMENT": [
            "film", "movie", "series", "drakor",
            "musik", "konser", "idol", "fandom",
            "lagu", "artis"
        ],
        "DOMAIN-FOOD": [
            "makan", "kuliner", "kopi", "ngopi",
            "resto", "restaurant", "warung", "food",
            "nasi", "jajan"
        ],
        "DOMAIN-LIFESTYLE": [
            "travel", "liburan", "fashion", "outfit",
            "gym", "workout", "healing", "lifestyle",
            "skincare"
        ],
        "DOMAIN-MEME": [
            "meme", "wkwk", "lol", "bjir", "bro",
            "core", "viral", "meme"
        ]
    }

    for domain, keywords in rules.items():
        if any(keyword in text or keyword in slang for keyword in keywords):
            return domain

    return "DOMAIN-SOCIAL"


def detect_generation(text, slang):
    text = normalize(text)
    slang = normalize(slang)

    alpha_markers = [
        "skibidi", "sigma", "gyatt", "rizz",
        "gwenchana", "sus", "npc"
    ]

    genz_markers = [
        "fomo", "yolo", "core", "slay",
        "valid", "spill", "relate", "gas",
        "menyala", "bjir", "gabut", "cees"
    ]

    millennial_markers = [
        "work", "office", "meeting", "deadline",
        "healing", "financial freedom",
        "frugal living"
    ]

    if any(x in text or x in slang for x in alpha_markers):
        return "GEN-ALPHA"

    if any(x in text or x in slang for x in genz_markers):
        return "GEN-Z"

    if any(x in text or x in slang for x in millennial_markers):
        return "GEN-MILLENNIAL"

    return "GEN-CROSS"


def detect_register(text, sentiment):
    text = normalize(text)
    sentiment = normalize(sentiment)

    if any(x in sentiment for x in ["sindiran", "sarcas"]):
        return "REG-SARCASTIC"

    if any(x in sentiment for x in ["humor", "terhibur"]):
        return "REG-HUMOR"

    if any(x in sentiment for x in ["marah", "frustr", "kesal"]):
        return "REG-EMOTIVE"

    if any(x in text for x in [
        "office", "meeting", "deadline",
        "client", "bos", "kerja"
    ]):
        return "REG-WORKPLACE"

    if any(x in text for x in [
        "twitter", "x ", "tiktok", "instagram",
        "viral", "post", "comment"
    ]):
        return "REG-INTERNET"

    return "REG-CASUAL"


def detect_code_switching(text):
    text = normalize(text)

    english_markers = [
        " literally ", " actually ", " honestly ",
        " vibe", " vibes", "core", "fomo", "yolo",
        "deadline", "meeting", "work", "office",
        "client", "ghosted", "red flag", "green flag",
        "financial freedom", "frugal living",
        "to the moon", "paylater", "gaming"
    ]

    sundanese_markers = [
        "teh", "mah", "atuh", "ieu", "eta",
        "kumaha", "euy", "punten"
    ]

    javanese_markers = [
        "rek", "ndak", "ora", "opo", "piye",
        "cok", "cak", "ndeso", "ngene"
    ]

    minangkabau_markers = [
        "uni", "uda", "awak", "lai"
    ]

    makassar_markers = [
        "ji", "mi", "ki", "ta", "kodong"
    ]

    manado_markers = [
        "jo", "pe", "so", "kita pe"
    ]

    if any(x in text for x in english_markers):
        return "CS-ID-EN"

    if any(x in text for x in sundanese_markers):
        return "CS-ID-SUN"

    if any(x in text for x in javanese_markers):
        return "CS-ID-JAV"

    if any(x in text for x in minangkabau_markers):
        return "CS-ID-MIN"

    if any(x in text for x in makassar_markers):
        return "CS-ID-MKS"

    if any(x in text for x in manado_markers):
        return "CS-ID-MAN"

    return "CS-NONE"


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
        "gaming": "ID-REG-GAMING",
        "komunitas gaming": "ID-REG-GAMING"
    }

    for location_name, cluster_id in mapping.items():
        if location_name in location:
            return cluster_id

    return "ID-REG-URBAN"


def main():
    dataset = load_json(DATASET_PATH)
    regional = load_json(REGIONAL_PATH)
    taxonomy = load_json(TAXONOMY_PATH)

    regional_ids = set(
        build_lookup(regional["clusters"]).keys()
    )

    taxonomy_ids = set()

    for dimension_items in taxonomy["dimensions"].values():
        taxonomy_ids.update(
            build_lookup(dimension_items).keys()
        )

    annotations = []
    seen_ids = set()

    for record in dataset:
        record_id = record["id"]

        if record_id in seen_ids:
            raise ValueError(
                f"Duplicate dataset ID detected: {record_id}"
            )

        seen_ids.add(record_id)

        text = record["konteks_percakapan"]
        slang = record["ragam_slang"]
        sentiment = record["sentimen_emosi"]
        location = record["lokasi_dominan"]

        regional_cluster = detect_regional_cluster(location)
        domain = detect_domain(text, slang)
        generation = detect_generation(text, slang)
        register = detect_register(text, sentiment)
        code_switching = detect_code_switching(text)

        annotation = {
            "id": record_id,
            "regional_cluster": regional_cluster,
            "domain": domain,
            "generation": generation,
            "register": register,
            "code_switching": code_switching
        }

        if regional_cluster not in regional_ids:
            raise ValueError(
                f"Unknown regional cluster: {regional_cluster}"
            )

        for field in [
            "domain",
            "generation",
            "register",
            "code_switching"
        ]:
            if annotation[field] not in taxonomy_ids:
                raise ValueError(
                    f"Unknown taxonomy ID: {annotation[field]}"
                )

        annotations.append(annotation)

    OUTPUT_PATH.write_text(
        json.dumps(
            annotations,
            ensure_ascii=False,
            indent=2
        ) + "\n",
        encoding="utf-8"
    )

    print(f"Dataset records : {len(dataset)}")
    print(f"Annotations     : {len(annotations)}")
    print(f"Output          : {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
