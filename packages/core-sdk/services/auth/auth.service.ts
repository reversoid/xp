import { User } from "../../models/user.js";
import { UserService } from "../user/user.service.js";
import { UserAlreadyExistsException } from "./errors.js";

export class AuthService {
  private readonly userService: UserService;

  constructor({ userService }: { userService: UserService }) {
    this.userService = userService;
  }

  async register(tgUserId: bigint, tgUsername: string): Promise<User> {
    const existingUser = await this.userService.getUserByTgId(tgUserId);

    if (existingUser) {
      throw new UserAlreadyExistsException();
    }

    return this.userService.createUser({
      tgId: tgUserId,
      tgUsername,
    });
  }
}
