import shutil
import sys
from pathlib import Path
from random import randrange

output_path = "./results/"


def main():
    participants: list[str] = collect_participants()
    results: dict[str, str] = assign_random(participants)
    assert_correctness(results, participants)
    prepare_output_folder()
    output_results(results)


def collect_participants() -> list[str]:
    input_args: list[str] = list(sys.argv)
    input_args.remove(input_args[0])
    input_args = list(set(input_args))
    print("These are the participants:\n" + "\n".join(input_args))
    return input_args


def assign_random(participants: list[str]):
    try:
        need_to_give: list[str] = list(participants)
        mapping: dict[str, str] = dict()
        for receiver in participants:
            mapping[receiver] = get_random_giver(receiver, need_to_give)
            need_to_give.remove(mapping[receiver])

        return mapping
    except RuntimeError as e:
        print(e)
        return assign_random(participants)


def get_random_giver(receiver: str, potential_givers):
    random_giver = potential_givers[randrange(len(potential_givers))]
    while random_giver == receiver:
        if len(potential_givers) == 1:
            raise RuntimeError("Last giver would be forced to give to himself!")
        random_giver = potential_givers[randrange(len(potential_givers))]
    return random_giver


def assert_correctness(result: dict[str, str], participants: list[str]):
    receivers: set[str] = set(result.keys())
    givers: set[str] = set(result.values())
    for recipient, giver in result.items():
        if recipient == giver:
            print("Error: recipient is giver!")
            exit(1)
    if len(receivers) != len(participants) or len(givers) != len(participants):
        print("Error: Not every participant is a recipient or giver!")  # because sets dont allow duplicates
        exit(1)


def prepare_output_folder():
    # remove output folder and create again to reset old results
    output_folder = Path(output_path)
    if output_folder.is_dir():
        shutil.rmtree(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)


def output_results(results: dict[str, str]):
    for recipient, giver in results.items():
        giver_file = Path(output_path + giver + ".txt")
        giver_file.write_text(recipient)
    print("Wrote results to /results folder.")


if __name__ == '__main__':
    main()
