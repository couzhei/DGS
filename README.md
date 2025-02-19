# ⚗️ DGS Project: Automation Initiative

This project aims to streamline and automate the process of account creation through modern Python tooling.

## 🔧 Requirements

- [uv](https://docs.astral.sh/uv/) - The lightning-fast Python package installer and resolver ⚡

## 🎯 Key Features

- 🔄 Fast dependency management
- 📦 Efficient package resolution
- 🔒 Reliable dependency locking
- ⚡ Lightning-fast virtual environments
- 🎨 Modern linting and formatting tools

## 🚀 Setup

1. **Install uv** 🛠️

   If you don't have `uv`, yet run this command:
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   

2. **Project Setup** 🏗️

   Simply run:
   ```sh
   uv run -m fastapi run
   ```
   And installation of packages will be taken care of as well as running your app in the **production** mode.

3. **Development Server** 💻

   Launch the FastAPI development server:
   ```sh
   uv run -m fastapi dev
   ```

## 📝 Managing Dependencies

### Adding New Packages 📦

```sh
uv add <package-name>
```

### Syncing Environment 🔄

```sh
uv sync
```


## 🚧 To-Dos

- [ ] **Completion**: Finalize all core functionality.
- [ ] **Writing Tests**: Develop comprehensive unit and integration tests.
- [ ] **Linting and Formatting**: Set up and enforce code style standards.
- [ ] **Containerization with Docker**: Create a Dockerfile and necessary configurations.
- [ ] **CI/CD with GitHub Actions**: Automate builds, tests, and deployments.
- [ ] **Writing Complete Documentation**: Prepare detailed usage and developer guides.
- [ ] **Structuring Project**: Review and improve overall project architecture.


<!-- ## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request -->

## 📚 Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/) 📖
- [FastAPI Documentation](https://fastapi.tiangolo.com/) 🚀
- [Python Package Index](https://pypi.org) 🐍
- [ruff](https://docs.astral.sh/ruff/tutorial/)⚖️
