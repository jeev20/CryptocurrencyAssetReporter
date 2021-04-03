*** Settings ***
Documentation   This robot returns the value of the crypto currency on the first day of the year. 
...             This can help in reporting taxes in Norway and may be other countries too. Thanks to Coingecko for an amazing free API.
Library  GetCryptoPortfolio.py
Library  RPA.Tables


*** Variables ***
${year}  2021
&{cryptoCurrencies}    Bitcoin=${2}  Cardano=${3000}   Ethereum=${23.093898}  Monero=${13}
${inFiatCurrency}  nok  # any fiat currency supported by CoinGecko

# +
*** Keywords ***
Get CryptoPortfolio Table
    ${portfolio} =  GetCryptoPortfolio  2021  ${cryptoCurrencies}   ${inFiatCurrency}

Read CryptoPortfolio Table
    ${portfolioTable} =  Read Table From Csv    output/CryptoPortfolio.csv
    
Create CryptoPortfolio Charts
    CreatePortfolioPieChart  ${inFiatCurrency}
    CreatePortfolioTreeMapChart  ${inFiatCurrency}
# -

*** Tasks ***
Obtain Portfolio Table and Visualize
  Get CryptoPortfolio Table
  Read CryptoPortfolio Table
  Create CryptoPortfolio Charts


