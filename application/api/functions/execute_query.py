from sql import queries
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