input = "d7_input.txt"

def count_with_wildcard(hand, target_count):
    wildcards = hand.count('J')
    if wildcards == 5:
        return True
    for card in set(hand):
        if card != 'J' and hand.count(card) + wildcards >= target_count:
            return True
    return False

def is_five_of_a_kind(hand):
    return count_with_wildcard(hand, 5)

def is_four_of_a_kind(hand):
    return count_with_wildcard(hand, 4)

def is_three_of_a_kind(hand):
    return count_with_wildcard(hand, 3)

def is_two_pairs(hand):
    pairs = 0
    wildcards = hand.count('J')
    used_wildcard = False
    for card in set(hand):
        if card != 'J':
            count = hand.count(card)
            if count + wildcards >= 2:
                pairs += 1
                if count == 1 and wildcards > 0 and not used_wildcard:
                    used_wildcard = True
                    wildcards -= 1
            if pairs == 2:
                return True
    return False

def is_one_pair(hand):
    return count_with_wildcard(hand, 2)

def is_full_house(hand):
    wildcards = hand.count('J')
    counts = {card: hand.count(card) for card in set(hand) if card != 'J'}

    # First, let's try to find a three of a kind or pair without using wildcards
    three_of_kind = None
    pair = None

    for card, count in counts.items():
        if count == 3:
            three_of_kind = card
        elif count == 2:
            pair = card

    # Use wildcard(s) if necessary
    if three_of_kind is None or pair is None:
        for card, count in counts.items():
            if count == 2 and three_of_kind is None and wildcards > 0:
                # Use wildcard to complete three of a kind
                three_of_kind = card
                wildcards -= 1
            elif count == 1 and pair is None and wildcards > 0:
                # Use wildcard to complete a pair
                pair = card
                wildcards -= 1

    return three_of_kind is not None and pair is not None and three_of_kind != pair





def all_cards_are_different(hand):
    seen = set()
    for card in hand:
        if card in seen and card != 'J':
            return False
        seen.add(card)
    return True


def sort_by_cards(hand_list):
    # Card rankings
    ranking = ["A", "K", "Q", "T", "10", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    rank_dict = {rank: index for index, rank in enumerate(ranking)}

    # Function to get the numeric rank of a hand
    def get_hand_rank(hand):
        return [rank_dict[card] for card in hand if card in rank_dict]

    # Sort the hands based on the first element of each sublist
    sorted_hands = sorted(hand_list, key=lambda x: get_hand_rank(x[0]), reverse=True)
    return sorted_hands




five_of_a_kind_bucket = []
four_of_a_kind_bucket = []
three_of_a_kind_bucket = []
full_house_bucket = []
two_pairs_bucket = []
one_pair_bucket = []
all_cards_diff_bucket = []

with open (input, "r") as f:
    for line in f:
        line = line.strip()
        cards_and_bid = line.split()
        if is_five_of_a_kind(cards_and_bid[0]):
            five_of_a_kind_bucket.append(cards_and_bid)
        elif is_four_of_a_kind(cards_and_bid[0]):
            four_of_a_kind_bucket.append(cards_and_bid)
        elif is_full_house(cards_and_bid[0]):
            full_house_bucket.append(cards_and_bid)
        elif is_three_of_a_kind(cards_and_bid[0]):
            three_of_a_kind_bucket.append(cards_and_bid)
        elif is_two_pairs(cards_and_bid[0]):
            two_pairs_bucket.append(cards_and_bid)
        elif is_one_pair(cards_and_bid[0]):
            one_pair_bucket.append(cards_and_bid)
        elif all_cards_are_different(cards_and_bid[0]):
            all_cards_diff_bucket.append(cards_and_bid)

five_of_a_kind_bucket = sort_by_cards(five_of_a_kind_bucket)
four_of_a_kind_bucket = sort_by_cards(four_of_a_kind_bucket)
full_house_bucket = sort_by_cards(full_house_bucket)
three_of_a_kind_bucket = sort_by_cards(three_of_a_kind_bucket)
two_pairs_bucket = sort_by_cards(two_pairs_bucket)
one_pair_bucket = sort_by_cards(one_pair_bucket)
all_cards_diff_bucket = sort_by_cards(all_cards_diff_bucket)

print(full_house_bucket)

rank = 1
total_winnings = 0
for bucket in [all_cards_diff_bucket, one_pair_bucket, two_pairs_bucket, three_of_a_kind_bucket, full_house_bucket, four_of_a_kind_bucket, five_of_a_kind_bucket]:
    for hand in bucket:
        hand.append(rank)
        print(hand)
        total_winnings += int(hand[1])*hand[2]
        rank += 1

print(is_full_house("A38JA"))

print(total_winnings)

#all_cards_diff_bucket, one_pair_bucket, two_pairs_bucket, three_of_a_kind_bucket, full_house_bucket, four_of_a_kind_bucket, five_of_a_kind_bucket