import argparse


def rank_league(filename: str):
    """
        Calculate the ranking table for a league.
    Args:
        filename (str): Name of the file from which to read the match results.
    """
    with open(filename) as file:
        match_results = file.read().splitlines()

    teams = {}
    for result in match_results:
        match = result.split(", ")
        team_a = " ".join(match[0].split(" ")[:-1])
        team_b = " ".join(match[1].split(" ")[:-1])

        team_a_scre = int(match[0].split(" ")[-1])
        team_b_scre = int(match[1].split(" ")[-1])

        if team_a_scre > team_b_scre:
            teams[team_a] = teams.get(team_a, 0) + 3
            teams[team_b] = teams.get(team_b, 0)

        elif team_a_scre < team_b_scre:
            teams[team_b] = teams.get(team_b, 0) + 3
            teams[team_a] = teams.get(team_a, 0)

        else:
            teams[team_a] = teams.get(team_a, 0) + 1
            teams[team_b] = teams.get(team_b, 0) + 1

    if teams:
        league_ranking = sorted(teams.items(), key=lambda entry: (-entry[1], entry[0]))

        team_pos = 1
        _, prev_pts = league_ranking[0]
        for team, cur_pts in league_ranking:
            if prev_pts != cur_pts:
                team_pos += 1

            prev_pts = cur_pts
            pt_suffix = "" if cur_pts == 1 else "s"

            print(f"{team_pos}. {team}, {cur_pts} pt{pt_suffix}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filename",
        action='store',
        type=str,
        help="Name of file containing the scores",
        required=True,
    )

    args = parser.parse_args()
    rank_league(filename=args.filename)