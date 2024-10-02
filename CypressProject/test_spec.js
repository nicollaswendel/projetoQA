describe('Página de exemplo', () => {
    it('Deve carregar a página inicial com sucesso', () => {
        cy.visit('https://example.cypress.io') // Abre a página de exemplo do Cypress
        cy.contains('type').click() // Clica em um link com o texto 'type'
        cy.url().should('include', '/commands/actions') // Verifica se a URL mudou
        cy.get('.action-email').type('teste@exemplo.com') // Digita em um campo de e-mail
        cy.get('.action-email').should('have.value', 'teste@exemplo.com') // Verifica se o e-mail foi inserido corretamente
    })
})