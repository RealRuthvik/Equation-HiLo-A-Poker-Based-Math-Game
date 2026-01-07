# **🧮 Equation Hi-Lo: Rules of the Game**

Welcome to Equation Hi-Lo, a game of strategy, betting, and quick math inspired by Netflix’s The Devil’s Plan.

In this version, you will compete against two opponents: a Bot Player and a Dealer Bot. Your goal is to build the best mathematical equation to win the pot of chips.

## **🎮 The Setup**

* **Players:** 3 Total (User, Bot Player, and Dealer Bot).  
* **The Deck:** Contains number cards (0–10) and four "suits" used for tie-breaking: Gold \> Silver \> Bronze \> Dirt.  
* **Operations:** You always have access to Addition (+), Subtraction (-), and Division (÷).  
* **Special Operations:** Multiplication (×) and Square Root (√) cards are hidden in the deck. If you draw one, it replaces one of your basic operations.

## **🔄 Gameplay Loop**

1. Ante & Private Card  
   Every player starts by putting 1 Chip into the pot (the Ante). You are then dealt one Private Card that only you can see.  
2. First Betting Round  
   Based on your one card, you can:  
   * **Check:** Stay in the game without adding chips (if no one else has bet).  
   * **Bet/Raise:** Add chips to the pot to increase the stakes.  
   * **Call:** Match the current highest bet to stay in the game.  
   * **Fold:** Give up your cards and your chips already in the pot.  
3. The Public Reveal  
   The dealer deals 3 Public Cards face-up for everyone to see.  
   * *Note: If you get a special card (× or √), the dealer will give you an extra number card to ensure you always have exactly 4 numbers to work with.*  
4. Final Betting Round  
   Now that you can see your opponents' public cards, there is one final round of betting to increase the pot.  
5. The Declaration  
   You must choose one of three targets for your final equation:  
   * **LOW:** You want your result to be as close to 1 as possible.  
   * **HIGH:** You want your result to be as close to 20 as possible.  
   * **SWING:** A high-risk move. You must have the best result for BOTH High and Low. If you lose either, you lose everything\!

## **🧮 Mathematical Rules**

This is where the game differs from standard math:

* **Left-to-Right Only:** Ignore PEMDAS/BODMAS. Equations are solved strictly from left to right.  
  * *Example: 2 \+ 3 \* 4 is 5 \* 4 \= 20 (not 14).*  
* **No Brackets:** You cannot use parentheses.  
* **Use Everything:** You must use all 4 number cards and 3 operation cards in your equation.  
* **Decimals Matter:** Results can be decimals or negative numbers. For example, 0.8 is considered closer to 1 than 1.5 is.

## **🏆 Winning & Tie-Breakers**

| Scenario | Outcome |
| :---- | :---- |
| **Split Pot** | If you go for High and an opponent goes for Low, you both win half the pot. |
| **Winner-Takes-All** | If you and an opponent choose the same target, the person closest to the target number wins the whole pot. |
| **Swing Win** | If you choose Swing and beat everyone at both High and Low, you take the entire pot. |
| **Swing Failure** | If you choose Swing but lose even one comparison (High or Low), your opponent wins the pot. |

**The Tie-Breaker:** If numerical results are identical, the winner is the person who used the card with the highest-ranking suit (Gold being the best).
