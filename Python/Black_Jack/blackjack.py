import random

# Card values (Aces can be 1 or 11)
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11
        else:
            value += card
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def show_hands(player, dealer, reveal_dealer=False):
    print("\nYour hand:", player, f"({calculate_hand_value(player)})")
    if reveal_dealer:
        print("Dealer's hand:", dealer, f"({calculate_hand_value(dealer)})")
    else:
        print("Dealer's hand:", [dealer[0], '❓'])

def blackjack():
    print("🎴 Welcome to Blackjack!")
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    show_hands(player, dealer)

    # Player's turn
    while True:
        choice = input("\nDo you want to (h)it or (s)tand? ").lower()
        if choice == 'h':
            player.append(deal_card())
            show_hands(player, dealer)
            if calculate_hand_value(player) > 21:
                print("💥 You busted! Dealer wins.")
                return
        elif choice == 's':
            break
        else:
            print("Please enter 'h' or 's'.")

    # Dealer's turn
    print("\nDealer's turn...")
    show_hands(player, dealer, reveal_dealer=True)
    while calculate_hand_value(dealer) < 17:
        dealer.append(deal_card())
        print("Dealer hits:", dealer)
    dealer_value = calculate_hand_value(dealer)
    player_value = calculate_hand_value(player)
    print(f"\nFinal Hands:")
    show_hands(player, dealer, reveal_dealer=True)

    # Determine winner
    if dealer_value > 21:
        print("🎉 Dealer busts! You win!")
    elif player_value > dealer_value:
        print("🎉 You win!")
    elif player_value < dealer_value:
        print("😞 Dealer wins!")
    else:
        print("🤝 It's a tie!")

def main():
    while True:
        blackjack()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing Blackjack!")
            break

if __name__ == "__main__":
    main()
