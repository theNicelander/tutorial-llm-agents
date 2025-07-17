import random


def mix_topic_samples(
    topics: dict[str, str],
    min_lines: int = 1,
    max_lines: int = 3,
) -> str:
    """Mix random samples from different topics into a single text.

    Args:
        topics: Dictionary mapping topic names to text lines
        min_lines: Minimum number of lines to sample from each topic
        max_lines: Maximum number of lines to sample from each topic

    Returns:
        Mixed text with random samples from each topic
    """
    secure_random = random.SystemRandom()
    mixed_sample_lines = []

    for text in topics.values():
        lines = text.splitlines()
        n = secure_random.randint(min_lines, max_lines)
        mixed_sample_lines.extend(secure_random.sample(lines, n))

    return "\n".join(mixed_sample_lines)
