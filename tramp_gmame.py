import random

def create_deck():
    marks = ['♠','♧','♦','♥']
    ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']

    deck = []
    for i in marks:
        for l in ranks:
            deck.append((i, l))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

#カードがなくなるまで配る
def deal_until_empty(deck, players = 2):
    hands = [[] for _ in range(players)]
    current_player = 0

    while deck:
        hands[current_player].append(deck.pop())
        current_player = (current_player + 1) % players

    return hands

#カードの強さ(数値化して強さを測る)
RANK_ORDER = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
RANK_POWER = {rank: i for i, rank in enumerate(RANK_ORDER)}

#カードの比較
def compare_cards(card1, card2):
    if RANK_POWER[card1[1]] < RANK_POWER[card2[1]]:
        return 1
    elif RANK_POWER[card1[1]] > RANK_POWER[card2[1]]:
        return -1
    else:
        return 0
    
#カードの表示
def card_to_text(card):
    mark, rank = card
    return f"{mark}の{rank}"


def play_war_game():
    print("戦争を開始します。")
    deck = create_deck()
    shuffle_deck(deck)
    hands = deal_until_empty(deck, players=2)
    p1_hand, p2_hand = hands[0], hands[1]

    p1_stock = []
    p2_stock = []

    print("カードが配られました。")

    while (p1_hand or p1_stock) and (p2_hand or p2_stock):
        #while内に作ることでtableは初期化できる
        table = []

        while True:
            if (not p1_hand and not p1_stock) or (not p2_hand and not p2_stock):
                break

            if not p1_hand:
                p1_hand = p1_stock
                p1_stock = []
                random.shuffle(p1_hand)

            if not p2_hand:
                p2_hand = p2_stock
                p2_stock = []
                random.shuffle(p2_hand)
           
            print("戦争！")

            p1_card = p1_hand.pop()
            p2_card = p2_hand.pop()


            #appendは×、リストの中にさらにリストが入ってしまう。[]で閉じる。引数は一つ
            table.extend([p1_card,p2_card])

            print(f"プレイヤー１のカードは{card_to_text(p1_card)}です。")
            print(f"プレイヤー２のカードは{card_to_text(p2_card)}です。")

            result = compare_cards(p1_card, p2_card)

            if result == 0:
                print("引き分けです。")
                #while Trueへ戻る
                continue
                    
                
            if result == 1:
                print("プレイヤー１が勝ちました。")
                p1_stock.extend(table)
            
            else:
                print("プレイヤー２が勝ちました。")
                p2_stock.extend(table)
            
            break

    print("戦争を終了します。")

    if not p1_hand:
        print("プレイヤー1の手札がなくなりました。")
    if not p2_hand:
        print("プレイヤー2の手札がなくなりました。")

    total1 = len(p1_hand) + len(p1_stock)
    total2 = len(p2_hand) + len(p2_stock)


    print(f"プレイヤー1の手札の枚数は{total1}枚です。")
    print(f"プレイヤー2の手札の枚数は{total2}枚です。")

    if total1 > total2:
        print("プレイヤー1が1位、プレイヤー2が2位です。")
    else:
        print("プレイヤー2が1位、プレイヤー1が2位です。")


play_war_game()

