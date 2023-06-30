import streamlit as st


def calc_returns(stake, odds):
    return round(stake * odds, 2)


def calc_net_profit(banked_amount, initial_stake):
    return banked_amount - initial_stake


def odds_to_decimal(odds_input):
    if '/' in odds_input:
        numerator, denominator = map(int, odds_input.split('/'))
        return numerator / denominator + 1
    else:
        return float(odds_input)


st.title("Betting Calculator")
st.write(
    "The aim is to win 5 bets on the trot, but only 2 need to win to show a banked return. The most you can lose is the initial stake.")

# Ask the user for the stake
stake = round(st.number_input("Please Enter a Stake for Bet 1", min_value=0.0, step=0.01), 2)

# Ask the user to enter the odds
odds_input = st.text_input("Please enter the odds for Bet 1 (as a decimal or fraction)")

# Check if odds_input is not empty
if odds_input:
    odds = odds_to_decimal(odds_input)
    st.write(f"Bet ({stake}) on the selection.")

    # Ask the user if the bet won or lost
    result = st.radio("Did Bet 1 win or lose?", ("", "Won", "Lost"))

    if result == "Lost":
        st.write("Better luck next time.")
        net_loss = calc_net_profit(0, stake)
        st.write(f"Net loss (taking into account initial stake): {net_loss}")
    elif result == "Won":
        # Calculate the returns
        returns = calc_returns(stake, odds)
        st.write(f"Congratulations! Your returns from Bet 1 are: {returns}")

        # Move on to Bet 2
        st.header("Bet 2")

        # The returns from Bet 1 become the stake for Bet 2
        stake2 = round(returns, 2)

        st.write(f"The returns from Bet 1 ({returns}) will be the stake for Bet 2.")

        # Ask the user to enter the odds for Bet 2
        odds_input2 = st.text_input("Please enter the odds for Bet 2 (as a decimal or fraction)")

        if odds_input2:
            odds2 = odds_to_decimal(odds_input2)

            st.write(f"Bet ({stake2}) on the selection.")

            # Ask the user if Bet 2 won or lost
            result2 = st.radio("Did Bet 2 win or lose?", ("", "Won", "Lost"))

            if result2 == "Lost":
                st.write("Better luck next time.")
                net_loss = calc_net_profit(returns, stake)
                st.write(f"Net loss (taking into account initial stake and returns from Bet 1): {net_loss}")
            elif result2 == "Won":
                # Calculate the returns from Bet 2
                returns2 = calc_returns(stake2, odds2)
                st.write(f"Congratulations! Your returns from Bet 2 are: {returns2}")

                # Move on to Bet 3
                st.header("Bet 3")

                # Bank a quarter of the returns from Bet 2
                banked = round(returns2 / 4, 2)
                st.write(f"Banking a quarter of the returns: {banked}")

                # The remaining returns become the stake for Bet 3
                stake3 = round(returns2 - banked, 2)
                st.write(f"The remaining amount ({stake3}) will be the stake for Bet 3.")

                # Ask the user to enter the odds for Bet 3
                odds_input3 = st.text_input("Please enter the odds for Bet 3 (as a decimal or fraction)")

                if odds_input3:
                    odds3 = odds_to_decimal(odds_input3)

                    st.write(f"Bet ({stake3}) on the selection.")

                    # Ask the user if Bet 3 won or lost
                    result3 = st.radio("Did Bet 3 win or lose?", ("", "Won", "Lost"))

                    if result3 == "Lost":
                        st.write("Better luck next time.")
                        net_loss = calc_net_profit(returns + returns2, stake)
                        st.write(
                            f"Net loss (taking into account initial stake and returns from Bet 1 and Bet 2): {net_loss}")
                    elif result3 == "Won":
                        # Calculate the returns from Bet 3
                        returns3 = calc_returns(stake3, odds3)
                        st.write(f"Congratulations! Your returns from Bet 3 are: {returns3}")

                        # Move on to Bet 4
                        st.header("Bet 4")

                        # Bank a third of the returns from Bet 3
                        banked2 = round(returns3 / 3, 2)
                        st.write(f"Banking a third of the returns: {banked2}")

                        # The remaining returns become the stake for Bet 4
                        stake4 = round(returns3 - banked2, 2)
                        st.write(f"The remaining amount ({stake4}) will be the stake for Bet 4.")

                        # Ask the user to enter the odds for Bet 4
                        odds_input4 = st.text_input("Please enter the odds for Bet 4 (as a decimal or fraction)")

                        if odds_input4:
                            odds4 = odds_to_decimal(odds_input4)

                            st.write(f"Bet ({stake4}) on the selection.")

                            # Ask the user if Bet 4 won or lost
                            result4 = st.radio("Did Bet 4 win or lose?", ("", "Won", "Lost"))

                            if result4 == "Lost":
                                st.write("Better luck next time.")
                                net_loss = calc_net_profit(returns + returns2 + returns3, stake)
                                st.write(
                                    f"Net loss (taking into account initial stake and returns from Bet 1, Bet 2, and Bet 3): {net_loss}")
                            elif result4 == "Won":
                                # Calculate the returns from Bet 4
                                returns4 = calc_returns(stake4, odds4)
                                st.write(f"Congratulations! Your returns from Bet 4 are: {returns4}")

                                # Move on to Bet 5
                                st.header("Bet 5")

                                # Bank half of the returns from Bet 4
                                banked3 = round(returns4 / 2, 2)
                                st.write(f"Banking half of the returns: {banked3}")

                                # The remaining returns become the stake for Bet 5
                                stake5 = round(returns4 - banked3, 2)
                                st.write(f"The remaining amount ({stake5}) will be the stake for Bet 5.")

                                # Ask the user to enter the odds for Bet 5
                                odds_input5 = st.text_input(
                                    "Please enter the odds for Bet 5 (as a decimal or fraction)")

                                if odds_input5:
                                    odds5 = odds_to_decimal(odds_input5)

                                    st.write(f"Bet ({stake5}) on the selection.")

                                    # Ask the user if Bet 5 won or lost
                                    result5 = st.radio("Did Bet 5 win or lose?", ("", "Won", "Lost"))

                                    if result5 == "Lost":
                                        st.write("Better luck next time.")
                                        net_loss = calc_net_profit(returns + returns2 + returns3 + returns4, stake)
                                        st.write(
                                            f"Net loss (taking into account initial stake and returns from Bet 1, Bet 2, Bet 3, and Bet 4): {net_loss}")
                                    elif result5 == "Won":
                                        # Calculate the returns from Bet 5
                                        returns5 = calc_returns(stake5, odds5)
                                        total_returns = returns + returns2 + returns3 + returns4 + returns5
                                        net_profit = calc_net_profit(total_returns, stake)
                                        st.write(f"Congratulations! Your total returns are: {total_returns}")
                                        st.write(
                                            f"Net profit (taking into account initial stake and banked amount): {net_profit}")
