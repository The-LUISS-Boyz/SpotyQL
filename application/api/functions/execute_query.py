from sql import queries, StrQuery
from sqlite3 import Error as SQLError

def execute_query(connection, i):
  try: 
    r = queries[i].execute_statement(connection)
    html = f"""
<span class="close-btn" onclick="closeResultBox(this)">X</span>
<pre><code>{r}</code></pre>
    """
    
    return html
  except SQLError as e:
    html = f"""
<span class="close-btn" onclick="closeResultBox(this)">X</span>
<pre><code class="language-sql">{e}</code></pre>
    """
    
    return html
  except Exception as e:
    raise e

def execute_query_str(connection, str):
  try:
    return StrQuery(str).execute_statement(connection)
  except SQLError as e:
    return str(e)
  except Exception as e:
    raise e
    