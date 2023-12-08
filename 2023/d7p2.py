input = "d7_input.txt"

def is_five_of_a_kind(hand):
    for i in range(len(hand)):
        if hand.count(hand[i]) == 5:
            return True
    return False

def is_four_of_a_kind(hand):
    for i in range(len(hand)):
        if hand.count(hand[i]) == 4:
            return True
    return False




def is_three_of_a_kind(hand):
    for i in range(len(hand)):
        if hand.count(hand[i]) == 3:
            return True
    return False



def is_two_pairs(hand):
    pair_count = 0
    for i in range(len(hand)):
        if hand.count(hand[i]) == 2:
            print(f"{hand[i]} has a pair in hand {hand}")
            pair_count += 1
    return pair_count == 4

def is_one_pair(hand):
    for i in range(len(hand)):
        if hand.count(hand[i]) == 2:
            return True
    return False

def is_full_house(hand):
    if is_three_of_a_kind(hand) and is_one_pair(hand):
        return True
    return False

def all_cards_are_different(hand):
    for i in range(len(hand)):
        if hand.count(hand[i]) > 1:
            return False    
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

# Example usage
hands = [['QQQJA', '483'], ['T55J5', '684']]
sorted_hands = sort_by_cards(hands)
print(sorted_hands)



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

rank = 1
total_winnings = 0
for bucket in [all_cards_diff_bucket, one_pair_bucket, two_pairs_bucket, three_of_a_kind_bucket, full_house_bucket, four_of_a_kind_bucket, five_of_a_kind_bucket]:
    for hand in bucket:
        hand.append(rank)
        print(hand)
        total_winnings += int(hand[1])*hand[2]
        rank += 1



print(total_winnings)