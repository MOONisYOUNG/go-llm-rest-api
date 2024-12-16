package main

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/gofiber/fiber/v2"
)

type User struct {
	Id   int
	Name string
}

var users map[int]User
var lastId int

func MakeWebHandler() *fiber.App {
	app := fiber.New()

	app.Get("/users", GetUserListHandler)
	app.Get("/users/:id", GetUserHandler)
	app.Post("/users", PostUserHandler)
	app.Delete("/users/:id", DeleteUserHandler)

	users = make(map[int]User)
	users[1] = User{1, "hide on bush"}
	users[2] = User{2, "kimoyi"}
	lastId = 2

	return app
}

type Users []User

func (s Users) Len() int {
	return len(s)
}
func (s Users) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s Users) Less(i, j int) bool {
	return s[i].Id < s[j].Id
}

func GetUserListHandler(c *fiber.Ctx) error {
	list := make(Users, 0)
	for _, User := range users {
		list = append(list, User)
	}
	sort.Sort(list)
	return c.Status(fiber.StatusOK).JSON(list)
}

func GetUserHandler(c *fiber.Ctx) error {
	id, err := strconv.Atoi(c.Params("id"))
	if err != nil {
		return c.SendStatus(fiber.StatusBadRequest)
	}

	User, ok := users[id]
	if !ok {
		return c.SendStatus(fiber.StatusNotFound)
	}
	return c.Status(fiber.StatusOK).JSON(User)
}

func PostUserHandler(c *fiber.Ctx) error {
	var user User
	if err := c.BodyParser(&user); err != nil {
		return c.SendStatus(fiber.StatusBadRequest)
	}
	lastId++
	user.Id = lastId
	users[lastId] = user
	return c.SendStatus(fiber.StatusCreated)
}

func DeleteUserHandler(c *fiber.Ctx) error {
	id, err := strconv.Atoi(c.Params("id"))
	if err != nil {
		return c.SendStatus(fiber.StatusBadRequest)
	}

	_, ok := users[id]
	if !ok {
		return c.SendStatus(fiber.StatusNotFound)
	}
	delete(users, id)
	return c.SendStatus(fiber.StatusOK)
}

func main() {
	fmt.Println("Starting server on :3000...")
	app := MakeWebHandler()
	if err := app.Listen(":3000"); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
