<br />
<div align="center">
  <a href='https://postimg.cc/w1KLLpP4' target='_blank'><img src='https://i.postimg.cc/w1KLLpP4/Add-a-subheading.gif' border='0' alt='Add-a-subheading'/></a>
  <h3 align="center">IPFSML</h3>
</div>

In the 2022-23 Octoverse report, we found that Python remains the second most-used programming language on GitHub. Interestingly, Python’s use grew more than 22 percent year over year with more than four million developers on GitHub using it at some point in 2022.

The web3 space for Python appears to have seen limited advancements, with a notable absence of protocol developers actively creating SDKs in the Python programming language.



## Problem
1. **Fragmented Web3 Protocol Ecosystem**: The increasing number of web3 protocols presents a challenge for users to access their services efficiently. With a growing variety of protocols, finding a unified platform to access and interact with these services becomes difficult.

2. **Lack of Python SDKs**: Despite the popularity of Python as a programming language, there is a noticeable absence of comprehensive SDKs that allow developers to interact with various web3 protocols seamlessly. This gap inhibits Python developers from easily integrating these protocols into their projects.

3. **Limited GraphQL SDKs**: Many web3 protocols provide APIs in GraphQL, which can offer powerful and flexible data querying. However, the availability of SDKs that provide well-designed, one-handed functions for easy GraphQL interaction with these protocols is limited, hindering efficient integration and usage.

4. **Barriers to Entry for Developers**: The absence of user-friendly SDKs and comprehensive resources can discourage developers from entering the web3 space. Without readily available tools to streamline the integration and utilization of web3 protocols, the barrier to entry remains high, potentially slowing down the adoption and growth of these protocols within the developer community.

## Solutions

To address the challenges mentioned earlier, we have developed the "Web3Toolkit," a comprehensive solution that aims to simplify the integration and utilization of various web3 protocols. This toolkit offers support for protocols such as Zora, Mode, and Covalent APIs through a Python SDK'S currently now, empowering developers in multiple ways:

1. **Unified Platform for Web3 Services**: The Web3Toolkit provides a centralized platform where developers can access a wide range of web3 protocols, including Zora, Mode, and Covalent. This unified approach streamlines the process of discovering and accessing services, eliminating the need to navigate multiple sources.

2. **Python SDK for Seamless Integration**: With the Web3Toolkit's Python SDK, developers can seamlessly integrate Zora, Mode, and Covalent protocols into their projects. This SDK offers a user-friendly interface that abstracts the complexities of interacting with these protocols, enabling Python developers to effortlessly leverage their functionalities.

3. **GraphQL Integration with One-Handed Functions**: The Web3Toolkit SDK is designed to include well-crafted, one-handed functions that facilitate GraphQL interactions with the supported protocols. This approach simplifies data querying and manipulation, making it easier for developers to extract the information they need for analytics dashboards, DApp data integrations, machine learning models, and more.

4. **Empowering Development Use Cases**: The Web3Toolkit empowers developers to create diverse applications, ranging from analytics dashboards that track protocol performance to machine learning models that leverage web3 data for predictions. By providing a streamlined integration process, the toolkit encourages innovative use cases and enables developers to explore the full potential of web3 protocols.

5. **Lowering Barriers for Adoption**: With the Web3Toolkit's user-friendly SDK and centralized platform, the barriers to entry for developers interested in web3 protocols are significantly reduced. This encourages a broader community of developers to engage with and contribute to the web3 ecosystem, fostering growth and innovation.

6. **Continuous Updates and Support**: The Web3Toolkit team is committed to maintaining and updating the toolkit to accommodate new protocols and enhancements. This ensures that developers can always access the latest capabilities and improvements, keeping their projects up-to-date with the evolving web3 landscape.

In summary, the "Web3Toolkit" addresses the challenges posed by the increasing number of web3 protocols by providing a Python SDK that supports Zora, Mode, and Covalent APIs currently. By offering a unified platform, easy integration, GraphQL support, and fostering a variety of development use cases, the toolkit empowers developers to harness the potential of web3 protocols and contribute to the growth of the web3 ecosystem.


## PIP PACKAGE

```!pip install Web3toolkit==1.0.4```

## ZORA PROTOCOL

Zora is a decentralized protocol where anyone can permissionlessly buy, sell, and create. We've created a series of tools that makes it easy to get started building.

Here the Web3toolkit ZORA PROTOCOL SDK ( EXAMPLE CALLS )
```

from Zora import sales, mints, help
mints = mints.mints_query_results('0xaa697E815F85Dd8C46b14EddfCB07f4A351d25BB',3,'PRICE')
print(mints)

```
help() function that describe the avilable functions and there parameters in detailed way.

( EXAMPLE CALLS )
```
mints.mints_query_results('0xaa697E815F85Dd8C46b14EddfCB07f4A351d25BB',3,'PRICE')
sales.sales_query_results('0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258',3,'OPENSEA_BUNDLE_SALE','TIME')
search.search_query_results('punk',10)
collection_metadata.collection_query_results("0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258")
events.events_query_results('0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258','91371','V3_RESERVE_AUCTION_EVENT', 5)
tokens.token_query_extract('0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258','60809')
agg_att.agg_att_query_results('0x60e4d786628fea6478f785a6d7e704777c86a7c6','7077')
agg_stats.agg_stats_query_results('0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb', 5)
off_chain.off_chain_query_results('0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258')
```


