package hello

import (
	"html/template"
	"net/http"
	"time"

	"appengine"
	"appengine/datastore"
)

type Greeting struct {
	Author  string `datastore:"author"`
	Content string `datastore:"content"`
	Date    time.Time `datastore:"date"`
}

func init() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/create", create_handler)
}

func handler(w http.ResponseWriter, r *http.Request) {
	c := appengine.NewContext(r)
	q := datastore.NewQuery("Greeting").Order("-date")
	greetings := make([]Greeting, 0, 10)
	if _, err := q.GetAll(c, &greetings); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if err := guestbookTemplate.Execute(w, greetings); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

var guestbookTemplate = template.Must(template.New("book").Parse(`
<html>
    <head>
        <title>Go Guestbook</title>
    </head>
    <body>
        {{range .}}
            <p class="author">{{.Author}}</p>
            <p>{{.Date}}</p>
            <pre>{{.Content}}</pre>
        {{end}}
    </body>
</html>
`))

func create_handler(w http.ResponseWriter, r *http.Request) {
	c := appengine.NewContext(r)
	g := Greeting{
		Content: "content",
		Author:  "auth1",
		Date:    time.Now(),
	}
	key := datastore.NewIncompleteKey(c, "Greeting", nil)
	_, err := datastore.Put(c, key, &g)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	http.Redirect(w, r, "/", http.StatusFound)
}
