# NOTIONPY
NOTION


## Usage
Quickstart
Note:
Need the latest version of NOTIONPY requires Python 3.5 or greater.
- Get your token from [notion my-integrations](https://www.notion.so/my-integrations)
- Create the dataset in notion, and share the current dataset with my-integration 
- 
![](https://github.com/wuchangsheng951/NOTIONPY/blob/main/share_example.png)

```
from NOTIONPY import NOTIONPY
# Get database ID from page URL

no = NOTIONPY(token,databaseId)

# update notion dataset column
no.update_column(['iou','data])

# update the value
no.add_col_value({'iou':'33',"Name":'hul2u','data':'233s2'})

```
