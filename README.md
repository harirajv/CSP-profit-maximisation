# CSP-profit-maximisation
Binary Search Cost Updation is a framework that can be used by Cloud service providers to compute the maximum price that can be charged for their services without having to lose out their trust rankings.

# Methodology
## AHP
Analytical Hierarchy Process (AHP) is a multi-criteria decision making mechanism. It simplifies decision making in problems that involve multiple factors in a quantitative manner.
For more details, visit https://en.wikipedia.org/wiki/Analytic_hierarchy_process

##Trust Ranking
Cloud Service Providers(CPS) are compared primarily using the Quality of Service(QoS) attributes. The QoS ratings provided by users for different CSPs can be used to compute rankings of the CSPs and thus compare their relative performances.

# Proposed Model
In BSCU, we attempt to find a higher price that a cloud service provider can charge for the same Quality of Service Attributes(QoS). We take the QoS requirements as the parameters for AHP ranking along with Price as one of the parameters. Since, an increase in the amount charged will cause a decrease in the Price rating for the CSP, we decrease the Price rating and compute the AHP ranks. The process is iterated until there is a change in the ranking of the CSP.

For usage, check the Example file.
